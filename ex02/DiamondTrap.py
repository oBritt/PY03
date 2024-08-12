from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """King of Everyone"""
    def __init__(self, first_name, is_alive=True):
        """Initialize a King"""
        # Lannister.__init__(self, first_name, is_alive)
        Baratheon.__init__(self, first_name, is_alive)

    def set_eyes(self, color):
        """set eye color"""
        self.eyes = color

    def set_hairs(self, hairs):
        """set hair color"""
        self.hairs = hairs

    def get_hairs(self):
        "returns hairs color"
        return self.hairs

    def get_eyes(self):
        "returns eyes color"
        return self.eyes
