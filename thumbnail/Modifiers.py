import itertools
from PIL import Image, ImageDraw, ImageFont


def draw_layer(img, color=(0, 0, 0, 80)):
    """
    Add a single-color layer on top of the image.

    Parameters
    ----------
    img: Image
        The original image.
    color: tuple(int, int, int, int)
        Color of the layer added, RGBA format.

    Returns
    -------
    downsize: Image
        A copy of the original image with the layer on top of it.
    """
    layer = Image.new('RGBA', img.size, color)
    return Image.alpha_composite(img, layer)


def downsize(img, max_w=0, max_h=0):
    """
    Downsize image, keep ratio.

    Parameters
    ----------
    img: Image
        The image to be downsized.
    max_w: int
        The maximum width of the downsized image.
    max_h: int
        The maximum height of the downsized image.

    Returns
    -------
    downsize: Image
        A downsized copy of the original image.
    """
    w = img.size[0]
    h = img.size[1]
    if max_w > 0 and w > max_w:
        h = h * (max_w / w)
        w = max_w
    if max_h > 0 and h > max_h:
        w = w * (max_h / h)
        h = max_h
    return img.resize((round(w), round(h)))


def draw_text(img, font, text, color=(255, 255, 255), border_color=(0, 0, 0)):
    """
    Draw text in the middle of the image.
    Font size will be automatically computed so that text cover 90% of
    the image width.

    Parameters
    ----------
    img: Image
        The original image.
    font: str
        Path of the font file.
    text: str
        Text to be printed on top of the image.
    color: tuple(int, int, int)
        Color of the text printed.
    border_color: tuple(int, int, int) or None
        Color of the border of the text. None for no border.

    Returns
    -------
    draw_text: Image
        A copy of the original image with the text on top.
    """
    img = img.copy()
    d = ImageDraw.Draw(img)
    # load font
    font_size = _find_font_size(img, font, text)
    font = ImageFont.truetype(font, font_size)
    # compute text coordinates for center
    w, h = d.textsize(text, font=font, spacing=40)
    w, h = (img.size[0] - w) / 2, (img.size[1] - h) / 2
    # draw border
    if border_color:
        for x, y in itertools.product([-1, 0, 1], repeat=2):
            d.text((w + x, h + y), text, font=font, align='center',
                   fill=(0, 0, 0), spacing=40)
    # draw text
    d.text((w, h), text, font=font, align='center', fill=color,
           spacing=40)
    return img


def _find_font_size(img, font, text):
    """
    Find the font size such that the text fills 90% of the
    image's width.
    """
    font_size = 512
    d = ImageDraw.Draw(img)
    # scale down
    w, h = img.size[0], img.size[1]
    while font_size > 0 and (w > img.size[0]*0.9 or h > img.size[1]*0.9):
        font_size = round(font_size / 2)
        imageFont = ImageFont.truetype(font, font_size)
        w, h = d.textsize(text, font=imageFont, spacing=40)
    # scale up
    while w < img.size[0]*0.9 and h < img.size[1]*0.9:
        font_size += 1
        imageFont = ImageFont.truetype(font, font_size)
        w, h = d.textsize(text, font=imageFont, spacing=40)
    font_size -= 1
    return font_size
