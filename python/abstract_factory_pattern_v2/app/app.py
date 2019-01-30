from python.abstract_factory_pattern_v2.factory.application_factory import ApplicationFactory

if __name__ == '__main__':
    watch_apple = ApplicationFactory("apple")
    music_player = watch_apple.get_music_player()
    print(music_player.play_music("Desperadoz"))
    android_phone = ApplicationFactory('android')
    android_photo = android_phone.get_photo_viewer()
    print(android_photo.show_photos('Vienna Karlsplatz'))
