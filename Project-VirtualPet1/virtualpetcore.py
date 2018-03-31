import random
import pickle
from constants import *


class VirtualPet:

    """The main class that represents a Virtual Pet object"""

    # ---------- Initialization & variables ----------

    def __init__(self):
        """Initialize the virtual pet"""
        # Variable format:
        # [lifePoints, happiness, hunger, health, weight, poop]
        self._vars = []
        pass

    @property
    def Happiness(self) -> int:
        try:
            return self._vars[1]
        except IndexError:
            pass
        return

    @Happiness.setter
    def Happiness(self, value: int):
        return

    # ---------- Tick things ----------
    def tick(self):
        """Periodically called, basically the "Life cycle" of the game"""
        pass

    # ---------- Player actions ----------
    def feed(self):
        pass

    def play_game(self):
        pass

    def visit_doctor(self):
        pass

    # ---------- Saving & loading ----------
    @staticmethod
    def save(self, virtual_pet: VirtualPet):
        pass

    @staticmethod
    def load(self, save_object) -> VirtualPet:
        pass

if __name__ == "__main__":
    # Text based Virtual Pet then
    from console_gui import main
    main()
