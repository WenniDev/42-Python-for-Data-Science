from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Representing the King family."""

    def __init__(self, first_name, is_alive=True):
        """King(str, bool=True)"""
        super().__init__(first_name, is_alive)

    def set_eyes(self, color):
        """set_eyes(str) -> None"""
        self.eyes = color

    def set_hairs(self, color):
        """set_hairs(str) -> None"""
        self.hairs = color

    def get_eyes(self):
        """get_eyes() -> str"""
        return self.eyes

    def get_hairs(self):
        """get_hairs() -> str"""
        return self.hairs
