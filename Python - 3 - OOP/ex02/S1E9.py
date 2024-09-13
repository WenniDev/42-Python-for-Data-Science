from abc import ABC, abstractmethod


class Character(ABC):
    """Representing a character"""

    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        """Character(str, bool=True)"""
        pass

    @abstractmethod
    def die(self):
        """die() -> None"""
        pass


class Stark(Character):
    """Representing the Stark family"""

    def __init__(self, first_name, is_alive=True):
        """Stark(str, bool=True)"""

        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """die() -> None"""
        self.is_alive = False
