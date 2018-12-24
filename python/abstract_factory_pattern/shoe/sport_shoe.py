from design_patterns.abstract_factory_pattern.shoe import shoe
from abc import ABCMeta


class SportShoe(shoe.Shoe):
    __metaclass__ = ABCMeta
