import abc


class HikingBoot(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def create_hiking_boot(self):
        pass
