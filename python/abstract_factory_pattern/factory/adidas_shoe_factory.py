from python.abstract_factory_pattern.brand.adidas_hiking_boot import AdidasHikingBoot
from python.abstract_factory_pattern.brand.adidas_sport_shoe import AdidasSportShoe
from python.abstract_factory_pattern.factory.shoe_factory import ShoeFactory


class AdidasShoeFactory(ShoeFactory):

    def __init__(self):
        super(AdidasShoeFactory, self).__init__();

    def create_hiking_boot(self):
        return AdidasHikingBoot()

    def create_sport_shoe(self):
        return AdidasSportShoe()
