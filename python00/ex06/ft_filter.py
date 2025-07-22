def ft_filter(func, iterable):
    """Return an iterator yielding items from the iterable
    for which func(item) is true. If func is None, return the items
    of the iterable that are truthy.

    Args:
        func (callable | None): A function that takes one argument and
            returns a boolean. If None, the identity function is assumed.
        iterable (iterable): An iterable whose elements will be filtered.

    Yields:
        object: Elements from the iterable for which func returns True,
        or that are truthy if func is None.
    """

    if func is None:
        res = [x for x in iterable if x]
    else:
        res = [x for x in iterable if func(x)]
    yield res


def is_even(n):
    return n % 2 == 0


# array = [2, 3, 4, "", 2, 1, 12, None, 75, 2, -3, 44]

if __name__ == "__main__":
    print(*ft_filter(None, [None, True, False, 0, 1]))
