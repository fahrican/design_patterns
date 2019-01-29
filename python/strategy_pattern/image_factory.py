from python.strategy_pattern.image_save_strategy import JpgStrategy, PngStrategy, GifStrategy


class ImageFactory:
    @staticmethod
    def save_image_in_specific_format(file_format):
        if file_format == 'jpg':
            return JpgStrategy()
        elif file_format == 'png':
            return PngStrategy()
        elif file_format == 'gif':
            return GifStrategy()
        else:
            assert 0, 'I am sorry I can\'t store the image in the given format.\n'