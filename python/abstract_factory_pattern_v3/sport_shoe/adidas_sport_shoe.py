from python.abstract_factory_pattern_v3.sport_shoe.sport_shoe import SportShoe


class AdidasSportShoe(SportShoe):

    def create_sport_shoe(self, model_name: str):
        return "This is the " + model_name + " Adidas sport shoe."
