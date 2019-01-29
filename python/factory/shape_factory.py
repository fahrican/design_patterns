from python.factory.circle import Circle
from python.factory.rectangle import Rectangle


class ShapeFactory:
    @staticmethod
    def get_shape(type_of_shape):
        if type_of_shape == 'circle':
            return Circle()
        elif type_of_shape == 'rectangle':
            return Rectangle()
        assert 0, 'There is no such a shape!!!'
