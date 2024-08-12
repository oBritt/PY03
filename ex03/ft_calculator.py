class calculator:
    "Calculator class"

    def __init__(self, arr) -> None:
        """initialize calculator"""
        self.arr = arr

    def __add__(self, object) -> None:
        """addition operator overload"""
        for i, e in enumerate(self.arr):
            self.arr[i] += object
        print(self.arr)

    def __mul__(self, object) -> None:
        """multiplication operator overload"""
        for i, e in enumerate(self.arr):
            self.arr[i] *= object
        print(self.arr)

    def __sub__(self, object) -> None:
        """subtraction operator overload"""
        for i, e in enumerate(self.arr):
            self.arr[i] -= object
        print(self.arr)

    def __truediv__(self, object) -> None:
        """division operator overload"""
        if object == 0:
            print("cant divide by Zero")
            return
        for i, e in enumerate(self.arr):
            self.arr[i] /= object
        print(self.arr)
