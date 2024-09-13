from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family"""

    def __init__(self, first_name, is_alive=True):
        """Baratheon(str, bool=True)"""

        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        """die() -> None"""
        self.is_alive = False

    def __str__(self):
        """__str__() -> str"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """__repr__() -> str"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"


class Lannister(Character):
    """Lannister class"""

    def __init__(self, first_name, is_alive=True):
        """Lannister(first_name, is_alive=True)"""

        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self):
        """die() -> None"""
        self.is_alive = False

    def __str__(self):
        """__str__() -> str"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """__repr__() -> str"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    @classmethod
    def create_lannister(cls, first_name, is_alive):
        """create_lannister(str, bool) -> Lannister"""
        return cls(first_name, is_alive)
