from design_patterns.decorater_pattern.decorator.car_decorater import CarDecorator
from design_patterns.decorater_pattern.helper.car import Car


class Radio(CarDecorator):
    car = None

    def __init__(self, car_brand: Car):
        self.car = car_brand

    def get_equipment(self) -> str:
        return '{0} with radio'.format(self.car.__class__.__name__)

    def get_price(self) -> float:
        return self.car.get_price() + 130.33
