NOTES = {
    "C": 0,
    "C#": 1,
    "D": 2,
    "D#": 3,
    "E": 4,
    "F": 5,
    "F#": 6,
    "G": 7,
    "G#": 8,
    "A": 9,
    "A#": 10,
    "B": 11,
}


def case():
    notes = [NOTES[x] for x in input().split()]
    diff = []
    for i in range(1, 4):
        diff.append(((notes[i] - notes[i - 1]) + 12) % 12)
    if diff == [4, 3, 3]:
        print("root")
    elif diff == [3, 3, 2]:
        print("first")
    elif diff == [3, 2, 4]:
        print("second")
    elif diff == [2, 4, 3]:
        print("third")
    else:
        print("invalid")


T = int(input())
for i in range(T):
    case()
