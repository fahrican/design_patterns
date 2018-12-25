from abc import ABCMeta, abstractmethod
from design_patterns.builder_pattern.model.robot import Robot


class RobotBuilder:
    __metaclass__ = ABCMeta

    @abstractmethod
    def build_robot_head(self):
        pass

    @abstractmethod
    def build_robot_torso(self):
        pass

    @abstractmethod
    def build_robot_arms(self):
        pass

    @abstractmethod
    def build_robot_legs(self):
        pass

    @abstractmethod
    def get_robot(self) -> Robot:
        pass
