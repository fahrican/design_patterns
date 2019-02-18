from python.abstract_factory_pattern.brand.nike_hiking_boot import NikeHikingBoot
from python.abstract_factory_pattern.brand.nike_sport_shoe import NikeSportShoe
from python.abstract_factory_pattern.factory.shoe_factory import ShoeFactory


class NikeShoeFactory(ShoeFactory):

    def create_hiking_boot(self):
        return NikeHikingBoot()

    def create_sport_shoe(self):
        return NikeSportShoe()
