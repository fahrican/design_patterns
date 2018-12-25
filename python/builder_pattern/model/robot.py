from design_patterns.builder_pattern.helper.robot_plan import RobotPlan


class Robot(RobotPlan):
    head = ''
    torso = ''
    arms = ''
    legs = ''

    def set_robot_head(self, head):
        self.head = head

    def set_robot_torso(self, torso):
        self.torso = torso

    def set_robot_arms(self, arms):
        self.arms = arms

    def set_robot_legs(self, legs):
        self.legs = legs
