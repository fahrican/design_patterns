from design_patterns.abstract_factory_pattern.factory import shoe_factory
from design_patterns.abstract_factory_pattern.brand import nike_sport_shoe, nike_hiking_boot


class NikeShoeFactory(shoe_factory.ShoeFactory):

    def create_shoe(self, type_of_shoe):
        if type_of_shoe == 'hiking':
            return nike_hiking_boot.NikeHikingBoot()
        elif type_of_shoe == 'sport':
            return nike_sport_shoe.NikeSportShoe()
        assert 0, 'There is no such a shoe!!!'
