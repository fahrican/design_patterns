from abc import ABCMeta, abstractmethod


class Shoe:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_shoe_name(self):
        pass
