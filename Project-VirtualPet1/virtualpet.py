import random
import pickle


class VirtualPet:

    """The main class that represents a Virtual Pet object"""

    # ---------- Initialization & variables ----------

    def __init__(self):
        """Initialize the virtual pet"""
        self.Happiness = 0
        self.Hunger = 0
        self.Health = 0
        self.Weight = 0
        self.LifePoints = 100
        pass

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
