from design_patterns.builder_pattern.model.robot_engineer import RobotEngineer
from design_patterns.builder_pattern.builder.old_robot_builder import OldRobotBuilder

if __name__ == '__main__':
    jarvis = OldRobotBuilder()
    tony_stark = RobotEngineer(jarvis)
    tony_stark.make_robot()
    friday = tony_stark.get_robot()
    print('Robot Built')
    print('Robot Head Type: {}'.format(friday.head))
    print('Robot Torso Type: {}'.format(friday.torso))
    print('Robot Arms Type: {}'.format(friday.arms))
    print('Robot Legs Type: {}'.format(friday.legs))
