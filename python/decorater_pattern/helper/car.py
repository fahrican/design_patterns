from abc import ABCMeta, abstractmethod


class Car:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_price(self) -> float:
        pass
