#!/usr/bin/python3
import abc

##########################################################################################
# This example is a robot speaker with multiple implementations using the Bridge pattern #
##########################################################################################


class RobotSpeaker:
    """This class is the abstraction to be implemented"""
    @abc.abstractmethod
    def speak(self):
        """This is the action to be implemented"""
        pass


class RobotSpeakerImplementation(RobotSpeaker):
    """This is the concrete implementation, where the implementor is selected"""
    def __init__(self, robot_speaker_implementor):
        self.robot_speaker = robot_speaker_implementor

    def speak(self):
        """Runs the implementation"""
        self.robot_speaker.speak()


class IRobotSpeakerImplementor:
    """This is the speaker implementor interface"""

    @abc.abstractmethod
    def speak(self):
        pass


class ConcreteSpeakImplementor1(IRobotSpeakerImplementor):
    """This is the first concrete implementation for speak"""
    def speak(self):
        print("BZZ HELLO WORLD! :]")


class ConcreteSpeakImplementor2(IRobotSpeakerImplementor):
    """This is the first concrete implementation for speak"""
    def speak(self):
        print("PTZZ ... HI WORLD! ~(o_o)~")


# Test
if __name__ == '__main__':
    # Creating implementations
    implementor1 = ConcreteSpeakImplementor1()
    implementor2 = ConcreteSpeakImplementor2()

    # Running the speaker and changing implementation
    robot_speaker = RobotSpeakerImplementation(implementor1)
    robot_speaker.speak()

    robot_speaker.robot_speaker = implementor2
    robot_speaker.speak()

