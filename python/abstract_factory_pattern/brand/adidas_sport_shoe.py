from design_patterns.abstract_factory_pattern.shoe import sport_shoe


class AdidasSportShoe(sport_shoe.SportShoe):

    def get_shoe_name(self):
        return 'Adidas sport shoe'
