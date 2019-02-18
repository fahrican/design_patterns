from abc import ABCMeta, abstractmethod


class HikingShoe:
    __metaclass__ = ABCMeta

    @abstractmethod
    def create_hiking_shoe(self, model_name: str):
        pass
