def naturals():
    """A generator function that yields the infinite sequence of natural
    numbers, starting at 1.

    >>> m = naturals()
    >>> type(m)
    <class 'generator'>
    >>> [next(m) for _ in range(10)]
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    i = 1
    while True:
        yield i
        i += 1


def scale(it, multiplier):
    """Yield elements of the iterable it scaled by a number multiplier.

    >>> m = scale([1, 5, 2], 5)
    >>> type(m)
    <class 'generator'>
    >>> list(m)
    [5, 25, 10]

    >>> m = scale(naturals(), 2)
    >>> [next(m) for _ in range(5)]
    [2, 4, 6, 8, 10]
    """
    "*** YOUR CODE HERE ***"
    yield from (x*multiplier for x in it)

# 生成器表达式: (f(item) for item in iter)    返回一个迭代器

def hailstone(n):
    """
    >>> for num in hailstone(10):
    ...     print(num)
    ...
    10
    5
    16
    8
    4
    2
    1
    """
    "*** YOUR CODE HERE ***"
    # while n != 1:
    #     if n % 2 == 0:
    #         n /= 2
    #         yield n
    #     else:
    #         n = 3*n + 1
    #         yield n
    # yield 1
    
    if n == 1:
        yield 1
    elif n % 2 == 0:
        yield n
        n = n // 2
        yield from hailstone(n)
    else:
        yield n
        n = 3 * n + 1
        yield from hailstone(n)
