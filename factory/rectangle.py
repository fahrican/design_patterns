from design_patterns.factory.shape_interface import ShapeInterface


class Rectangle(ShapeInterface):
    def draw(self):
        print("draw a rectangle")
