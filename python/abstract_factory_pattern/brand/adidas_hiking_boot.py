from design_patterns.abstract_factory_pattern.shoe import hiking_boot


class AdidasHikingBoot(hiking_boot.HikingBoot):

    def get_shoe_name(self):
        return 'Adidas hiking boot'
