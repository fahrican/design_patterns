from python.abstract_factory_pattern_v3.hiking_shoe.hiking_shoe import HikingShoe


class AdidasHikingShoe(HikingShoe):

    def create_hiking_shoe(self, model_name: str):
        return "This is the " + model_name + " Adidas hiking shoe."
