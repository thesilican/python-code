import functools


def memoize(obj):
    cache = obj.cache = {}

    @functools.wraps(obj)
    def memoizer(*args, **kwargs):
        if args not in cache:
            cache[args] = obj(*args, **kwargs)
        return cache[args]
    return memoizer


@memoize
def ack(m, n):
    print("ack({} {})".format(m, n))
    return n + 1 if m == 0 else (ack(m - 1, 1) if n == 0 else ack(m-1, ack(m, n-1)))


for i in range(1, 5):
    for j in range(1, 5):
        try:
            print(ack(i, j))
        except:
            pass
