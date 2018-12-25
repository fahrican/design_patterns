from design_patterns.decorater_pattern.decorator.car_decorater import CarDecorator
from design_patterns.decorater_pattern.helper.car import Car


class LeatherSeats(CarDecorator):
    car = None

    def __init__(self, car_brand: Car):
        self.car = car_brand

    def get_equipment(self) -> str:
        return '{} with leather seats'.format(self.car.__class__.__name__)

    def get_price(self) -> float:
        return self.car.get_price() + 530.66
