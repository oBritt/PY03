from S1E9 import Character


class Baratheon(Character):
    """Baratheon person class"""

    def __init__(self, first_name, is_alive=True):
        """Initializing Baratheon"""
        super().__init__(first_name, is_alive)
        self.last_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"


class Lannister(Character):
    """mighty person Lannister"""

    def __init__(self, first_name, is_alive=True):
        """initializing Lannister"""
        super().__init__(first_name, is_alive)
        self.last_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    @classmethod
    def create_lannister(cls, first_name, is_alived=True):
        """creates instance of Lannisters"""
        return cls(first_name, is_alived)
