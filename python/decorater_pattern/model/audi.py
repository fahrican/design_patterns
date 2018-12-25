from design_patterns.decorater_pattern.helper.car import Car


class Audi(Car):
    equipment = ''

    def __init__(self):
        self.equipment = 'Audi A6'

    def get_price(self) -> float:
        return 50000

    def brand_of_car(self) -> str:
        return self.equipment
