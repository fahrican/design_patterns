from abc import ABCMeta, abstractmethod


class MusicPlayer:
    __metaclass__ = ABCMeta

    def __init__(self):
        super(MusicPlayer, self).__init__()

    @abstractmethod
    def play_music(self, song: str):
        pass
