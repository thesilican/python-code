print(sum(
    [
        sum(
            filter(lambda x: x % 2 == 0, [
                int(n) for n in str(i)
            ])
        ) 
        for i in range(1, 100 + 1)
    ])
)

s = 0
for i in range(1, 100 + 1):
    nums = (int(n) for n in str(i))
    sum_ = sum(filter(lambda x: x % 2 == 0, nums))
    print(i, sum_, s)
    s += sum_
print(s)