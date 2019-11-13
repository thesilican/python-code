for n in range(240, 301):
    i = 0
    while i ** 2 <= n:
        j = 0
        while j <= i:
            if (i**2) + (j**2) == n:
                print(f"{n} = {i**2} + {j**2}")
            j += 1
        i += 1