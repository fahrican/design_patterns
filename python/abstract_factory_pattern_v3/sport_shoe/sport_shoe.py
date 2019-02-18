from abc import ABCMeta, abstractmethod


class SportShoe:
    __metaclass__ = ABCMeta

    @abstractmethod
    def create_sport_shoe(self, model_name: str):
        pass
