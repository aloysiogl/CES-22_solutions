#!/usr/bin/python3
import abc

##############################################################################################
# This is an example of two different robots communicating using the Mediator design pattern #
##############################################################################################


class CommunicationMediator:
    """Communication mediator"""
    def communicate(self, message, caller):
        pass


class CommunicationConcreteMediator(CommunicationMediator):
    """Communication concrete mediator"""
    def __init__(self, commander,  explorer):
        self.commander = commander
        self.explorer = explorer

    def communicate(self, message, caller):
        if caller.__class__.__name__ == "ExplorerRobot":
            self.commander.receive(message)
        if caller.__class__.__name__ == "CommanderRobot":
            self.explorer.receive(message)


class Robot:
    """The colleague class"""
    def __init__(self, mediator):
        self.communication_mediator = mediator

    def speak(self, message):
        self.communication_mediator.communicate(message, self)

    @abc.abstractmethod
    def receive(self, message):
        pass


class ExplorerRobot(Robot):
    """Explorer robot"""
    def __init__(self, mediator):
        super().__init__(mediator)

    def receive(self, message):
        print("Explorer receiving: " + message)


class CommanderRobot(Robot):
    """Command robot"""

    def __init__(self, mediator):
        super().__init__(mediator)

    def receive(self, message):
        print("Commander receiving: " + message)


# Test
if __name__ == '__main__':
    # Instantiating robots and mediator
    commander = CommanderRobot(CommunicationMediator())
    explorer = ExplorerRobot(CommunicationMediator())
    mediator = CommunicationConcreteMediator(commander, explorer)
    commander.communication_mediator = mediator
    explorer.communication_mediator = mediator

    # Sending messages to each other
    commander.speak("Send me the status of the misson...")
    explorer.speak("Status is exploring terrain...")
    commander.speak("Ok, keep me updated...")
    explorer.speak("Shutting down communication temporarily...")
