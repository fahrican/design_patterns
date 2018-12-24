from design_patterns.abstract_factory_pattern.shoe import hiking_boot


class NikeHikingBoot(hiking_boot.HikingBoot):

    def get_shoe_name(self):
        return 'Nike hiking boot'
