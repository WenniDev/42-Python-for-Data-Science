class calculator:

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        # Ensure both vectors have the same length
        if len(V1) != len(V2):
            raise ValueError("Both vectors must have the same length")
        result = sum(a * b for a, b in zip(V1, V2))
        print(f"Dot product is: {result}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        # Ensure both vectors have the same length
        if len(V1) != len(V2):
            raise ValueError("Both vectors must have the same length")
        result = [float(a + b) for a, b in zip(V1, V2)]
        print(f"Add Vector is : {result}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        # Ensure both vectors have the same length
        if len(V1) != len(V2):
            raise ValueError("Both vectors must have the same length")
        result = [float(a - b) for a, b in zip(V1, V2)]
        print(f"Sous Vector is: {result}")
