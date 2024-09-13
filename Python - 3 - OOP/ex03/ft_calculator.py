class calculator:
    """Calculator class."""

    def __init__(self, vector) -> None:
        self.vector = vector

    def __add__(self, object) -> None:
        """Add x to number to the vector."""
        self.vector = [x + object for x in self.vector]
        print(self.vector)
        return self.vector

    def __mul__(self, object) -> None:
        """Multiply x to number to the vector."""
        self.vector = [x * object for x in self.vector]
        print(self.vector)
        return self.vector

    def __sub__(self, object) -> None:
        """Subtract x to number to the vector."""
        self.vector = [x - object for x in self.vector]
        print(self.vector)
        return self.vector

    def __truediv__(self, object) -> None:
        """Divide x to number to the vector."""
        if (object == 0):
            raise ZeroDivisionError("division by zero")
        self.vector = [x / object for x in self.vector]
        print(self.vector)
        return self.vector
