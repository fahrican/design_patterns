from abc import ABCMeta, abstractmethod


class ShoeFactory:
    __metaclass__ = ABCMeta

    def __init__(self):
        super(ShoeFactory, self).__init__()

    @abstractmethod
    def create_hiking_boot(self):
        pass

    @abstractmethod
    def create_sport_shoe(self):
        pass
