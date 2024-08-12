class calculator:
    """Best calculator"""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Dot product"""
        total = 0
        for i, e in enumerate(V1):
            total += V1[i] * V2[i]
        print(f"Dot product is: {total}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Addition of two lists"""
        temp = []
        for i, e in enumerate(V1):
            temp.append(V1[i] + V2[i])
        print(f"Add Vector is : {temp}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Subtraction of two lists"""
        temp = []
        for i, e in enumerate(V1):
            temp.append(V1[i] - V2[i])
        print(f"Sous Vector is : {temp}")
