import os

from . import ImageBank
from . import SentenceBank
from .Modifiers import *


def generate(images, sentences, font, output):
    """
    Take sentences and put them on top of images, ready to be published
    on Facebook, Linkedin, Twitter, etc. Each sentence in the `sentences`
    file is written on top of an image randomly picked from the `images`
    folder.

    Parameters
    ----------
    images: str
        Path of the folder containing the images.
    sentences: str
        Path of the file containing the sentences, with one sentence per
        line.
    font: str
        Path of the font file.
    output: str
        Path of the folder where the output images will be stored.
    """
    images = ImageBank.load(images)
    sentences = SentenceBank.load(sentences)

    for i, sentence in enumerate(sentences):
        img = images.random()
        img = downsize(img, 1200, 1200)
        img = draw_layer(img, color=(96, 126, 180, 190))
        img = draw_text(img, font, sentence)
        img.save(os.path.join(output, 'image_{}.png'.format(i)))
