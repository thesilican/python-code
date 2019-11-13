from random import randint
from typing import List
import time

# Trying out some OOP UwU


class Die:
    """A simple class representing a singular die
    """

    def __init__(self, sides: int) -> None:
        if sides <= 1:
            raise Exception("Die must have at least 2 sides")
        self._sides = sides

    def roll(self) -> int:
        return randint(1, self._sides)

    @property
    def sides(self):
        return self._sides


class DiceRollResults:
    """Represents the result of a dice roll
    """

    def __init__(self, dice: List[Die], results: List[int]) -> None:
        self.dice = dice
        self.results = results

    @property
    def sum(self):
        return sum(self.results)

    @property
    def avg(self):
        return self.sum / len(self.results)

    @property
    def max(self):
        return max(self.results)

    @property
    def min(self):
        return min(self.results)

    def __iter__(self):
        return zip(self.dice, self.results)


class DiceCollection:
    """Represents a small collection of dice
    """

    def __init__(self):
        self.dice: List[Die] = []

    def addDie(self, die: Die):
        self.dice.append(die)

    def removeDie(self, index: int = -1):
        if index == -1:
            self.dice.pop()
        else:
            self.dice.pop(index)

    def roll(self) -> DiceRollResults:
        results = [x.roll() for x in self.dice]
        return DiceRollResults(self.dice, results)
    
    def __iter__(self):
        return iter(self.dice)
    
    def __len__(self):
        return len(self.dice)


class DiceRollResults:
    """Represents the result of a dice roll
    """

    def __init__(self, dice: List[Die], results: List[int]) -> None:
        self.dice = dice
        self.results = results
        self._iterIndex = 0

    @property
    def sum(self):
        return sum(self.results)

    @property
    def avg(self):
        return self.sum / len(self)

    @property
    def max(self):
        return max(self.results)

    @property
    def min(self):
        return min(self.results)

    def __iter__(self):
        return zip(self.dice, self.results)

    def __next__(self):
        if self._iterIndex >= len(self):
            raise StopIteration
        else:
            index = self._iterIndex
            self._iterIndex += 1
            return (self.dice[index], self.results[index])
    
    def __len__(self):
        return len(self.dice)

def main():
    """Main Program"""
    def displayMenu(options, prompt) -> int:
        print(prompt)
        selected = -1
        maxOption = len(options)
        while selected == -1:
            for index, txt in enumerate(options):
                print(f"{index + 1} {txt}")
            selected = int(input())
            if selected >= maxOption or selected < 1:
                selected = -1
                continue
        return selected - 1  # For 0-based indexing

    def createDie():
        print("Enter the number of sides for your new die: ", end="")
        sides = int(input())
        die = Die(sides)
        dice.addDie(die)

    def viewDice():
        print("You have the following dice:")
        printList = [f"D{d.sides}" for d in dice.dice]
        print(*printList, sep=" ")

    def removeDie():
        if len(dice) == 0:
            print("You have no dice to remove!")
            return
        for index, d in enumerate(dice):
            print(f"{index + 1} D{d.sides}")

        val = -1
        while val == -1:
            print("Enter which die you would like to remove: ")
            val = int(input())
            if val < 1 or val > len(dice):
                val = -1
        dice.removeDie(val - 1)

    def rollDice():
        print("Rolling dice...", flush=True)
        time.sleep(1)

        res = dice.roll()
        print("Results:")
        for r in res:
            print(f"D{r[0].sides} - {r[1]}")
        print("Sum:", res.sum, "Average:", res.avg)

    # Main program loop
    dice: DiceCollection = DiceCollection()
    while True:
        options = [
            "Create new die",
            "View dice",
            "Remove die",
            "Roll dice",
            "Exit"
        ]
        funcs = [
            createDie,
            viewDice,
            removeDie,
            rollDice,
        ]
        selected = displayMenu(options, "\nSelect an Option:")
        if selected == 4:
            break
        else:
            print() # Newline
            funcs[selected]()


if __name__ == "__main__":
    main()
