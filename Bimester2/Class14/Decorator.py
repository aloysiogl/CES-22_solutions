#!/usr/bin/python3
import abc


################################################################################
# This example is a robot sound maker using decorators to extend functionality #
# observe that the decorator is implemented from scratch and python default    #
# decorator in not used                                                        #
################################################################################

class IRobotSpeaker:
    """Robot interface"""
    @abc.abstractmethod
    def speak(self):
        pass


class SimpleRobotSpeaker(IRobotSpeaker):
    """Simple robot speaker"""
    def speak(self):
        print("HELLO WORLD", end="")


class DecoratedRobotSpeaker(IRobotSpeaker):
    """Decorated robot speaker"""
    def __init__(self, robot_speaker):
        self.robot_speaker = robot_speaker

    def speak(self):
        self.robot_speaker.speak()


class LazyRobot(DecoratedRobotSpeaker):
    """Lazy robot speaker"""

    def __init__(self, robot_speaker):
        super().__init__(robot_speaker)

    def speak(self):
        super(LazyRobot, self).speak()
        print(" ~(o_o)~", end="")


class BrokenRobot(DecoratedRobotSpeaker):
    """Broken robot speaker"""

    def __init__(self, robot_speaker):
        super().__init__(robot_speaker)

    def speak(self):
        super(BrokenRobot, self).speak()
        print(" ¥[*.*]¥", end="")


# Test
if __name__ == '__main__':
    # Creating main speaker
    simple_robot_speaker = SimpleRobotSpeaker()

    # Creating decorated lazy robot
    lazy_robot = LazyRobot(simple_robot_speaker)

    # Creating decorated broken robot
    broken_robot = BrokenRobot(simple_robot_speaker)

    # Testing each speech
    simple_robot_speaker.speak()
    print()
    lazy_robot.speak()
    print()
    broken_robot.speak()
    print()
