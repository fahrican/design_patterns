from python.abstract_factory_pattern_v2.music_player.music_player import MusicPlayer


class AndroidMusicPlayer(MusicPlayer):

    def __init__(self):
        super(AndroidMusicPlayer, self).__init__()

    def play_music(self, song: str):
        return "Running " + song + " on Google Play Music"
