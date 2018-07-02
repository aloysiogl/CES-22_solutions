#!/usr/bin/python3
import abc

#################################################################################
# This is an example of robot factory using the design pattern Abstract Factory #
#################################################################################


class AbstractRobotFactory:
    """Abstract factory"""
    @abc.abstractmethod
    def createRobot(self):
        pass


class AbstractRobot:
    """Abstract robot"""
    @abc.abstractmethod
    def show(self):
        pass


class FriendlyRobot(AbstractRobot):
    """Shows a friendly robot"""
    def show(self):
        print(":|]")


class EnemyRobot(AbstractRobot):
    """Shows an enemy robot"""
    def show(self):
        print("  _i_")
        print(" -|O|-")
        print("/ |_|")
        print(" |   |")


class FriendlyFactory(AbstractRobotFactory):
    """Creates friendly robots"""
    def createRobot(self):
        return FriendlyRobot()


class EnemyFactory(AbstractRobotFactory):
    """Creates enemy robots"""
    def createRobot(self):
        return EnemyRobot()


# Test
if __name__ == '__main__':
    # Using the friendly factory
    abstract_factory = FriendlyFactory()

    # Printing friendly robot
    abstract_factory.createRobot().show()

    # Print separator
    print("#######")

    # Using enemy factory
    abstract_factory = EnemyFactory()

    # Printing enemy robot
    abstract_factory.createRobot().show()