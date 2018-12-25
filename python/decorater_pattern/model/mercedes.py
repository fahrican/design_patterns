from design_patterns.decorater_pattern.helper.car import Car


class Mercedes(Car):
    equipment = ''

    def __init__(self):
        self.equipment = 'Mercedes SLS'

    def get_price(self) -> float:
        return 200000

    def brand_of_car(self) -> str:
        return self.equipment
