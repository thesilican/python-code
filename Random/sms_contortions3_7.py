from fractions import Fraction
sum = Fraction(0)
for i in range(33):
    d = (i**2) + (7 * i) + 12
    print(d)
    sum += Fraction(12, d)
print (f"sum = {sum}")