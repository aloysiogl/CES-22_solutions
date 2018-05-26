#!/usr/bin/python3

import abc


class GameObject:

    game_objects_list = []

    def __init__(self, transform):
        """
        Every game object must be associated with a position rotation and scale
        :param transform: the transform quantities for the object
        """
        self.transform = transform

    @abc.abstractmethod
    def start(self):
        """
        This method runs once the object is instantiated
        """
        pass

    @abc.abstractmethod
    def update(self):
        """
        This method runs each frame
        """
        pass

    @abc.abstractmethod
    def draw(self):
        """
        This codes draws the game object in the screen
        """
        pass

    @classmethod
    def clear_game_objects_list(cls):
        """
        This method clears the game objects list
        """

        cls.game_objects_list = []

    @staticmethod
    def extract_vector(transform):
        """
        This method extracts a vector from a transform
        :param transform: the transform to extract the vector
        :return: a vector2
        """

        return transform.position
