from python.strategy_pattern.image_factory import ImageFactory

if __name__ == '__main__':
    print('Type a specific format like JPG, PNG ect. to store image:')
    print('Your choice: ', end='')
    user_input = input()
    any_image = ImageFactory.save_image_in_specific_format(user_input.lower().strip())
    any_image.save_image()
