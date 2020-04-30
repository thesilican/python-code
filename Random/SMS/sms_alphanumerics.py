# Link: https://tio.run/##dVRNa9wwEL37VwzKRWq9S0Kby8L2UigEUigkPZR0MYotbxRkyUhysv7125HkzzQRGFvM15v3Ztz2/snoL@fzBdzU0JsOXrn24A2UT1wfBch44dB0ystWyZJ7aTS01jwq0eTZBXxPjuQHV06Q4E3ubSdIlt3cFT9/397f/Lr9A3uI9mw4tTUN@L6V@giyaY31cCudz7JK1GBFq3gpikoepXfUeYtuO8B3Ptoaob3bQSVLz2DzDaT2uwzwWOE7q8OdErJ9NlLThrdU8eax4nCKWegyycPpwEDWcMKYVXYQiBcIySEBYIwleIUz6kXQTnPn5FGLCpMKn8N8DbDykaNd7OwBkxxYwojVlNCLBAz2e7hMxnB01zhkTGHcEj02/JaauSqbCiLOMREi7aJe@5hz25qWLqxdU6AFXzRYIw3aeFjqFkkoiqRRUVBSd7r0xihH2NaKqivFRG4O/Q5On/o8FpvrYNpUaj8BmnsNpzYWZOA/xK1N4bQ2yBmEk1jzuUNWrq5zAmTR6exH9gQ@R5nHYlPQ1xw@imL/ASrzhMlh46KiI89b6UXjKGMf4SxzRICx72IjM34gmwBl8kqTm634qKXywi6m9xQFQssE54WrTiAeXI2wh/TqcgktzVgQWfjlwE0OgzlMLH3f@pDC0uwc0FdO5tUmpFGcpzAtS/L4cBVW@NjUvAstjkHZSpUoyZr7MF/ebqXjqn3itHxHmqEHXlW03CrziqQOY/Cmh0gEW3YxfCHG5Rq4PiyA85XUuAa8onjB3yNK/FcTlg1ybzabu2EIHX6jYcUHO595L7LxEdz1/wA
# If you want to change it to a multiplication problem,
# Change "False" to "True"

IS_MULTIPLY = False







from typing import List

def replace_digits(string: str, replacements: dict) -> int:
    return int("".join(map(lambda x: str(replacements[x]) if x in replacements else "", string)))

def _solve(unassigned: set, assigned: dict, problem: List[str]):
    if len(unassigned) == 0:
        nums = list(map(lambda s: replace_digits(s, assigned), problem))
        solution = nums.pop()
        sum_ = sum(nums) if not IS_MULTIPLY else __import__("functools").reduce(lambda x, y: x*y, nums)
        if sum_ == solution:
            for i in nums:
                print(str(i).rjust(15," "))
            print("=" + str(solution).rjust(14, " "))
            print()
            for c, i in sorted(assigned.items()):
                print(c,"=", i)
            print("".rjust(15, "-"))

        return
    for i in filter(lambda x: x not in assigned.values(), range(10)):
        unassi = set(unassigned)
        assi = dict(assigned)
        assi[unassi.pop()] = i
        _solve(unassi, assi, problem)

def solve(problem: List[str]):
    unassi = set()
    for s in problem:
        for c in s:
            if str.isalpha(c):
                unassi.add(c.lower())
    _solve(unassi, dict(), problem)

problem = __import__("sys").stdin.read().split("\n")
print("---Solutions---")
solve(problem)
print("---------------")