from design_patterns import image_save_strategy

if __name__ == '__main__':
    print('Type a number to save image in special format')
    print('1) .jpg')
    print('2) .png')
    print('3) .gif')
    print('Your choice: ', end='')
    user_input = int(input())
    any_image = None

    if user_input == 1:
        any_image = image_save_strategy.JpgStrategy()
    elif user_input == 2:
        any_image = image_save_strategy.PngStrategy()
    elif user_input == 3:
        any_image = image_save_strategy.GifStrategy()
    else:
        assert 0, 'Type a number between 1 - 3!!!'

    any_image.save_image()
