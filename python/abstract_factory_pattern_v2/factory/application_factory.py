from python.abstract_factory_pattern_v2.music_player.android_music_player import AndroidMusicPlayer
from python.abstract_factory_pattern_v2.photo_viewer.android_photo_viewer import AndroidPhotoViewer
from python.abstract_factory_pattern_v2.music_player.apple_music_player import AppleMusicPlayer
from python.abstract_factory_pattern_v2.photo_viewer.apple_photo_viewer import ApplePhotoViewer


class ApplicationFactory:

    def __init__(self, plat):
        self.platform = plat

    def get_music_player(self):
        music_dict = {
            "apple": AppleMusicPlayer(),
            "android": AndroidMusicPlayer()
        }
        return music_dict[self.platform]

    def get_photo_viewer(self):
        photo_dict = {
            "apple": ApplePhotoViewer(),
            "android": AndroidPhotoViewer()
        }
        return photo_dict[self.platform]
