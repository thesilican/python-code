import random
import pickle
import constants as const


class VirtualPet:

    """The main class that represents a Virtual Pet object"""

    # ---------- Initialization & variables ----------

    def __init__(self):
        """Initialize the virtual pet"""
<<<<<<< Updated upstream:Project-VirtualPet1/virtualpetcore.py
        # Variable format:
        # [lifePoints, happiness, hunger, health, weight, poop]
        self.create()
        pass

    def create(self):
        """Creates a new virtual pet with initial settings"""
        self._pet_vars = const.VARIABLES_INIT.copy()
        self.age = 0

    def get_var(self, index: int) -> int:
        return self._pet_vars[index]

    def set_var(self, index: int, value: int):
        self._pet_vars[index] = min(const.VARIABLES_MIN[index], max(
            const.VARIABLES_MAX[index], value))

    # ---------- Tick things ----------

=======
        self.__happiness = 0
        self.__hunger = 0
        self.__health = 0
        self.__weight = 0
        self.__lifePoints = 100
        self.__Poop = 100
        pass

    @property
    def Happiness(self):
        return self.__happiness

    @Happiness.setter
    def Happiness(self, value):

        # ---------- Tick things ----------
>>>>>>> Stashed changes:Project-VirtualPet1/virtualpet.py
    def tick(self):
        """Periodically called, basically the "Life cycle" of the game"""
        pass

    # ---------- Player actions ----------
    def feed(self):
        """Feed your pet periodically to keep him from going hungry!
        Feeding him too fast, however, may cause him to grow overweight
        """

        pass

    def play_game(self):
        """Play a mini-game with your pet to keep him happy & healthy!
        """

        pass

    def visit_doctor(self):
        """Pets don't always like checkups, but it's necissary for your pet's health!
        """

        pass

    # ---------- Saving & loading ----------
    @staticmethod
    def save(self, virtual_pet: VirtualPet, file_path: str) -> None:
        pass

    @staticmethod
    def load(self, file_path: str) -> VirtualPet:
        pass


<<<<<<< Updated upstream:Project-VirtualPet1/virtualpetcore.py
if __name__ == "__main__":
    # Text based Virtual Pet then
    from console_gui import main
    main()
=======
# if __name__ == "__main__":
#     # Text based Virtual Pet then
#     from console_gui import main
#     main()
>>>>>>> Stashed changes:Project-VirtualPet1/virtualpet.py
