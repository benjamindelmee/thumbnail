import functools
import os
import random
from PIL import Image


class ImageBank():
    """
       List-like object of images.
       The images used are loaded on the fly (lazy computing)
    """

    def __init__(self):
        self._bank = []

    def __iter__(self):
        self._iter = iter(self._bank)
        return self

    def __next__(self):
        return self._load_from_file(next(self._iter))

    def random(self):
        return self._load_from_file(random.choice(self._bank))

    def _list_folder(self, folder):
        for filename in os.listdir(folder):
            self._bank.append(os.path.join(folder, filename))

    @functools.lru_cache(maxsize=64)
    def _load_from_file(self, path):
        return Image.open(path).convert('RGBA')


def load(folder):
    """Returns a list-like object of images fetched from a folder"""
    bank = ImageBank()
    bank._list_folder(folder)
    return bank
