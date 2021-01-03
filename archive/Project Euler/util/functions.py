import inspect
import functools


def memoize(func=None, pos=0, name="", nameKey=""):
    """
    Memoization decorator for a function.

    You can either use the decorator directly, or specify which
    argument you would like to decorate

    Examples:
    `@memoize def factorial(n)`
    Memoizes the factorial function


    `@memoize("n") def getName(self, n)`
    Memoizes the argument 'n' of the getName function
    """
    # Meta-programming is confusing
    if callable(func):
        decorator = memoize()
        return decorator(func)
    else:
        # This is the actual decorator
        # This whole function is actually a meta-decorator
        def memoizedecorator(func):
            argPos = pos
            if name != "":
                funcProps = inspect.getfullargspec(func)[0]
                try:
                    argPos = funcProps.index(name)
                except ValueError:
                    raise "Func " + str(func) + \
                        " does not have parameter " + name
            argNameKey = nameKey
            cache = func.cache = {}
            if argNameKey != "":
                @functools.wraps(func)
                def memoizedfunc(**kwargs):
                    if argNameKey not in kwargs:
                        return func(**kwargs)
                    elif kwargs[argNameKey] not in cache:
                        cache[kwargs[argNameKey]] = func(**kwargs)
                    return cache[kwargs[argNameKey]]
                return memoizedfunc
            else:
                @functools.wraps(func)
                def memoizedfunc(*args):
                    if len(args) <= argPos:
                        return func(*args)
                    elif args[argPos] not in cache:
                        cache[args[argPos]] = func(*args)
                    return cache[args[argPos]]
                return memoizedfunc
        return memoizedecorator
