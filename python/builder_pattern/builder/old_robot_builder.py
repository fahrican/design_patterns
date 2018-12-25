from design_patterns.builder_pattern.builder.robot_builder import RobotBuilder
from design_patterns.builder_pattern.model.robot import Robot


class OldRobotBuilder(RobotBuilder):
    robot = None

    def __init__(self):
        self.robot = Robot()

    def build_robot_head(self):
        self.robot.set_robot_head('Iron Head')

    def build_robot_torso(self):
        self.robot.set_robot_torso('Iron Torso')

    def build_robot_arms(self):
        self.robot.set_robot_arms('Blowtorch Arms')

    def build_robot_legs(self):
        self.robot.set_robot_legs('Roller Skates')

    def get_robot(self) -> Robot:
        return self.robot
