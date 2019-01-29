from python.factory.shape_factory import ShapeFactory

if __name__ == '__main__':
    print('Enter type of shape: ', end='')
    type_of_shape = input()
    the_shape = ShapeFactory.get_shape(type_of_shape)
    the_shape.draw()
