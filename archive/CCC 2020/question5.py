input()
people = [int(x) for x in input().split()]
burgers = dict()
for i, p in enumerate(people):
    if p not in burgers:
        burgers[p] = 0
    burgers[p] += 1

coachFavorite = people[0]
joshFavorite = people[-1]


def totalBurgers(burgs):
    count = 0
    for val in burgs.values():
        count += val
    return count


def chance(ppl, burgs):
    personFav = ppl[0]
    total = totalBurgers(burgs)
    # Chance of the person picking their favorite
    chanceSum = 0
    for val in burgs.keys():
        if burgs[val] == 0:
            continue
        if personFav == val:
            chanceSum += burgs[val]
        elif coachFavorite == val:
            chanceSum += burgs[val]
        elif joshFavorite == val:
            chanceSum += 0
        else:
            # Keep taking burgers until you get a person
            # without a burger
            pplCopy = ppl[1:]
            burgCopy = burgs.copy()
            burgCopy[val] -= 1
            while True:
                if len(pplCopy) == 0:
                    chanceSum += 1 * burgs[p]
                    break
                p = pplCopy[0]
                if burgCopy[p] == 0:
                    chanceSum += chance(pplCopy, burgCopy) * burgs[p]
                    break
                else:
                    burgCopy[p] -= 1
                    pplCopy.pop(0)
    return chanceSum/total

if joshFavorite == coachFavorite:
    print(1)
else:
    response = chance(people, burgers)
    print(response)
