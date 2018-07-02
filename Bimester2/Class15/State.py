#!/usr/bin/python3
import abc

######################################################################################################
# This is an example of State design pattern, It is a light bulb and there are two states on and off #
######################################################################################################


class ButtonState:
    """Abstract class for holding the button state to control the light bulb"""
    def __init__(self, bulb):
        self.bulb = bulb

    @abc.abstractmethod
    def press(self):
        pass


class On(ButtonState):
    """State for turning on the light bulb"""
    def __init__(self, bulb):
        super().__init__(bulb)

    def press(self):
        self.bulb.setState(Off(self.bulb))
        print("Light turned off ( )")


class Off(ButtonState):
    """State for turning off the light bulb"""
    def __init__(self, bulb):
        super().__init__(bulb)

    def press(self):
        self.bulb.setState(On(self.bulb))
        print("Light turned on  (i)")


class LightBulb:
    """Light bulb to be controlled by the button"""
    def __init__(self):
        self.state = Off(self)

    def setState(self, state):
        self.state = state

    def press(self):
        self.state.press()


# Test
if __name__ == '__main__':
    # Creating a light bulb
    light_bulb = LightBulb()

    # Turning on and off the light bulb
    light_bulb.press()
    light_bulb.press()
    light_bulb.press()
    light_bulb.press()
    light_bulb.press()