from abc import ABC, abstractmethod


class Character(ABC):
    """Base class"""

    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        """initializer Character"""
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """function makes char dead"""
        self.is_alive = False


class Stark(Character):
    """very important Stark class"""

    def __init__(self, first_name, is_alive=True):
        """initialize Stark class"""
        super().__init__(first_name, is_alive)
