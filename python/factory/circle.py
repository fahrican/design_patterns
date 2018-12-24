from design_patterns.factory.shape_interface import ShapeInterface


class Circle(ShapeInterface):
    def draw(self):
        print("draw a circle")
