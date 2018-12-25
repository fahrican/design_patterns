from design_patterns.builder_pattern.builder.robot_builder import RobotBuilder
from design_patterns.builder_pattern.model.robot import Robot


class RobotEngineer:
    robot_builder = None

    def __init__(self, robot_builder: RobotBuilder):
        self.robot_builder = robot_builder

    def get_robot(self) -> Robot:
        return self.robot_builder.get_robot()

    def make_robot(self):
        self.robot_builder.build_robot_head()
        self.robot_builder.build_robot_torso()
        self.robot_builder.build_robot_arms()
        self.robot_builder.build_robot_legs()
