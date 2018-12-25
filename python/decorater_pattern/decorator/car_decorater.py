from design_patterns.decorater_pattern.helper.car import Car
from abc import ABCMeta, abstractmethod


class CarDecorator(Car):
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_equipment(self) -> str:
        pass
