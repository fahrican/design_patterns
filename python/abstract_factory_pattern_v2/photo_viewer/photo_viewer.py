from abc import ABCMeta, abstractmethod


class PhotoViewer:
    __metaclass__ = ABCMeta

    def __init__(self):
        super().__init__()

    @abstractmethod
    def show_photos(self, img: str):
        pass
