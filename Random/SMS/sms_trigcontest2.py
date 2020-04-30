import math


def heron(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s-a) * (s-b) * (s-c))

def angles(a, b, c):
    A = 180 * math.acos((-a**2 + b**2 + c**2) / (2 * b * c)) / math.pi
    B = 180 * math.acos((a**2 - b**2 + c**2) / (2 * b * c)) / math.pi
    C = 180 * math.acos((a**2 + b**2 - c**2) / (2 * b * c)) / math.pi
    return [A, B, C]

for i in range(1, 16):
    for j in range(i, 16):
        for k in range(j, 16):
            if (i + j <= k or j + k <= i or i + k <= j):
                continue
            area = heron (i, j, k)
            if (area.is_integer()):
                angs = angles(i, j, k);
                if (angs[0].is_integer() or angs[1].is_integer() or angs[2].is_integer()):
                    print(f"Sides: {i} {j} {k} Area: {heron(i,j,k)} Angles: {angles(i, j, k)}")