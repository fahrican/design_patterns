from design_patterns.abstract_factory_pattern.factory import shoe_factory
from design_patterns.abstract_factory_pattern.brand import adidas_hiking_boot, adidas_sport_shoe


class AdidasShoeFactory(shoe_factory.ShoeFactory):

    def create_shoe(self, type_of_shoe):
        if type_of_shoe == 'hiking':
            return adidas_hiking_boot.AdidasHikingBoot()
        elif type_of_shoe == 'sport':
            return adidas_sport_shoe.AdidasSportShoe()
        assert 0, 'There is no such a shoe!!!'
