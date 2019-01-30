from python.abstract_factory_pattern_v2.photo_viewer.photo_viewer import PhotoViewer


class AndroidPhotoViewer(PhotoViewer):

    def __init__(self):
        super().__init__()

    def show_photos(self, img: str):
        return "Displaying " + img + " on Google Photos"
