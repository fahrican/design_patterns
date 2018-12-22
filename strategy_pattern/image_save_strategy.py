from abc import ABCMeta, abstractmethod


class ImageSaveStrategy:
    __metaclass__ = ABCMeta

    @abstractmethod
    def save_image(self):
        pass


class PngStrategy(ImageSaveStrategy):

    def save_image(self):
        print('Save image as a .png')


class JpgStrategy(ImageSaveStrategy):

    def save_image(self):
        print('Save image as a .jpg')


class GifStrategy(ImageSaveStrategy):

    def save_image(self):
        print('Save image as a .gif')
