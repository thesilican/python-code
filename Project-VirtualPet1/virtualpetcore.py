import random
import pickle
from constants import LIFEPOINTS, HAPPINESS, HUNGER, HEALTH, WEIGHT, POOP
import constants as const


class VirtualPet:

    """The main class that represents a Virtual Pet object"""

    # ---------- Initialization & variables ----------

    def __init__(self):
        """Initialize the virtual pet"""
        # Variable format:
        # [lifePoints, happiness, hunger, health, weight, discipline, poop]
        self.create()
        pass

    def create(self):
        """Creates a new virtual pet with initial settings"""
        self._pet_vars = const.VARIABLES_INIT.copy()
        self.age = 0

    def get_var(self, index: int) -> int:
        return self._pet_vars[index]

    def set_var(self, index: int, value: int):
        self._pet_vars[index] = min(0, max(
            const.VARIABLES_MAX[index], value))

    def change_var(self, index: int, amount: int):
        self.set_var(index, self.get_var(index) + amount)

    # ---------- Tick things ----------

    def tick(self):
        """Periodically called, basically the "Life cycle" of the game
            Should be called something like once every 5 seconds"""
        self.age += 1

        # Do things like slowly decrease Happiness, Health, Weight
        # Increase hunger
        pass

    def _tick_poop(self):
        if random.randint(1, 20) == 1:
            self.change_var(POOP, 1)

        # ---------- Player actions ----------
    def feed(self):
        """Feed your pet periodically to keep him from going hungry!
        Feeding him too fast, however, may cause him to grow overweight
        """

        pass

    def play_game(self, success: int):
        """Play a game with your pet to keep him healthy & active!

        Arguments:
            success {int} -- from 0-3, how successful the player was at playing the game
        """
        if success == 0:
            pass
        elif success == 1:
            pass
        elif success == 2:
            pass
        elif success == 3:
            pass

    def visit_doctor(self):
        """Pets don't always like checkups, but it's necissary for your pet's health!
        """

        pass

    def clean_poop(self) -> bool:
        """Cleans your Pet's filthy poop (if any)
        You pet is happy after you clean out the poop
        Returns:
            bool -- Successfully clean some poop
        """
        if self.get_var(POOP) > 0:
            self.set_var(POOP, 0)
            self.change_var(HAPPINESS, 5)
            return True
        return False

    # ---------- Saving & loading ----------
    @classmethod
    def save(self, virtual_pet: 'VirtualPet', file_path: str) -> None:
        pickle.dump(virtual_pet, file_path)

    @classmethod
    def load(self, file_path: str) -> 'VirtualPet':
        return pickle.load(file_path)


if __name__ == "__main__":
    # Text based Virtual Pet then
    from console_gui import main
    main()
