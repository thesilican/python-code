year = 1901
day = 2 # Sunday = 7
month = 1

MONTHS = {
    1:31,
    2:28,
    3:31,
    4:30,
    5:31,
    6:30,
    7:31,
    8:31,
    9:30,
    10:31,
    11:30,
    12:31
}

acc = 0
while year != 2000 or month != 12:
    if day % 7 == 0:
        acc += 1
    day += MONTHS[month]
    if month == 2 and year % 4 == 0 and\
        (year % 100 != 100 or year % 400 == 0):
        day += 1
    month += 1
    if month > 12:
        month = 1
        year += 1
print(acc)
