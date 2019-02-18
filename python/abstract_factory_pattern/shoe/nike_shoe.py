import abc


class NikeShoe(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def create_nike_shoe(self):
        pass
