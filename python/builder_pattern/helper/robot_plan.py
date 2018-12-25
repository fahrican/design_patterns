from abc import ABCMeta, abstractmethod


class RobotPlan:
    __metaclass__ = ABCMeta

    @abstractmethod
    def set_robot_head(self, head):
        pass

    @abstractmethod
    def set_robot_torso(self, torso):
        pass

    @abstractmethod
    def set_robot_arms(self, arms):
        pass

    @abstractmethod
    def set_robot_legs(self, legs):
        pass
