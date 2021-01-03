import random

MIN = 1
MAX = 100
MAX_TRIES = 6

num = random.randint(MIN, MAX)
tries = MAX_TRIES
print("Arrr ye maties... I'm thinkin' of a number from " + str(MIN) + " to " + str(MAX))
while tries > 0:
    print("You have " + str(tries) + " tries. What's yur guess?\n> ", end = "")
    guess = int(input())
    if guess == num:
        print("Avast! You guessed it!")
        break
    elif guess > num:
        print("Shiver me timbers... too big!")
    elif guess < num:
        print("Shiver me timbers... too small!")
    tries -= 1
