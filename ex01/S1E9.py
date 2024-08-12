from abc import ABC, abstractmethod


class Character(ABC):
    """Base class"""

    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        """initializer Character"""
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """die function"""
        self.is_alive = False

    def __str__(self) -> str:
        return f"Vector ('{self.last_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self) -> str:
        return self.__str__()


class Stark(Character):
    """very important Stark class"""

    def __init__(self, first_name, is_alive=True):
        """initialize Stark class"""
        super().__init__(first_name, is_alive)
