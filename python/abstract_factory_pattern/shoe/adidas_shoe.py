import abc


class AdidasShoe(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def create_adidas_shoe(self):
        pass
