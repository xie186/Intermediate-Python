def flip_list(a, inplace=False):
    """
    Flip (reverse) a list.

    Parameters
    ----------
    a : list 
        List to be reversed.
    inplace : bool, optional
        Specifies whether to flip the list "in place",
        or return a new list (default).

    Returns
    -------
    flipped : list (or None)
        The flipped list. If `inplace=True`, None is returned.


    >>> flip_list([1, 2, 3])
    [3, 2, 1]

    >>> a = [1, 2, 3]
    >>> flip_list(a, inplace=True)
    >>> a
    [3, 2, 1]
    """
    if inplace is True:
        a[:] = a[::-1]
        return None
    else:
        return a[::-1]
