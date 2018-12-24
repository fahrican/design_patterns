from abc import ABCMeta, abstractmethod


class ShoeFactory:
    __metaclass__ = ABCMeta

    @abstractmethod
    def create_shoe(self, type_of_shoe):
        pass
