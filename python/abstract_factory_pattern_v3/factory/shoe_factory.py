from python.abstract_factory_pattern_v3.hiking_shoe.adidas_hiking_shoe import AdidasHikingShoe
from python.abstract_factory_pattern_v3.hiking_shoe.nike_hiking_shoe import NikeHikingShoe
from python.abstract_factory_pattern_v3.sport_shoe.adidas_sport_shoe import AdidasSportShoe
from python.abstract_factory_pattern_v3.sport_shoe.nike_sport_shoe import NikeSportShoe


class ShoeFactory:

    def __init__(self, brand):
        self.brand = brand

    def get_hiking_shoe(self):
        hiking_dict = {
            'nike': NikeHikingShoe(),
            'adidas': AdidasHikingShoe()
        }
        return hiking_dict[self.brand]

    def get_sport_shoe(self):
        sport_dict = {
            'nike': NikeSportShoe(),
            'adidas': AdidasSportShoe()
        }
        return sport_dict[self.brand]
