```
def add_trees(t1, t2):

    """

    >>> numbers = tree(1,

    ...                [tree(2,

    ...                      [tree(3),

    ...                       tree(4)]),

    ...                 tree(5,

    ...                      [tree(6,

    ...                            [tree(7)]),

    ...                       tree(8)])])

    >>> print_tree(add_trees(numbers, numbers))

    2

      4

        6

        8

      10

        12

          14

        16

    >>> print_tree(add_trees(tree(2), tree(3, [tree(4), tree(5)])))

    5

      4

      5

    >>> print_tree(add_trees(tree(2, [tree(3)]), tree(2, [tree(3), tree(4)])))

    4

      6

      4

    >>> print_tree(add_trees(tree(2, [tree(3, [tree(4), tree(5)])]), \

    tree(2, [tree(3, [tree(4)]), tree(5)])))

    4

      6

        8

        5

      5

    """

    "*** YOUR CODE HERE ***"

    # res_label = label(t1) + label(t2)

    # res_branch = []

    # i = 0

    # while i < len(branches(t1)) and i < len(branches(t2)):

    #     b1, b2 = branches(t1)[i], branches(t2)[i]

    #     new_branch = add_trees(b1, b2)

    #     res_branch += [new_branch]

    #     i += 1

    # res_branch += branches(t1)[i:]

    # res_branch += branches(t2)[i:]

    # return tree(res_label, res_branch)

  

    res_label = label(t1) + label(t2)

    res_branch = []

    for b1, b2 in zip(branches(t1), branches(t2)):

        new_branch = add_trees(b1, b2)

        res_branch += [new_branch]

    i = len(res_branch)

    res_branch += branches(t1)[i:]

    res_branch += branches(t2)[i:]

    return tree(res_label, res_branch)
```

```
def berry_finder(t):

    """Returns True if t contains a node with the value 'berry' and

    False otherwise.

  

    >>> scrat = tree('berry')

    >>> berry_finder(scrat)

    True

    >>> sproul = tree('roots', [tree('branch1', [tree('leaf'), tree('berry')]), tree('branch2')])

    >>> berry_finder(sproul)

    True

    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])

    >>> berry_finder(numbers)

    False

    >>> t = tree(1, [tree('berry',[tree('not berry')])])

    >>> berry_finder(t)

    True

    """

    "*** YOUR CODE HERE ***"

    if is_leaf(t):

        if label(t) == 'berry': return True

        return False

    elif label(t) == 'berry': return True

    else:

        for branch in branches(t):

            if berry_finder(branch): return True

        return False
```