import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Truncates a 2D list (like a matrix) by slicing rows
    from index 'start' to 'end'.

    Args:
        family (list): A 2D list of numbers (e.g., height and weight).
        start (int): The starting row index (inclusive).
        end (int): The ending row index (exclusive).

    Raises:
        AssertionError: If the input is not a list of equal-length lists.

    Returns:
        list: A truncated 2D list containing rows from index 'start' to 'end'.
    """
    try:
        if not isinstance(family, list):
            raise AssertionError
        if not all(len(row) == len(family[0]) for row in family):
            raise AssertionError
        t_lst = np.array(family)
        print("My shape is :", t_lst.shape)
        trunc = t_lst[start:end]
        print("My new shape is :", trunc.shape)
        return trunc.tolist()
    except AssertionError:
        print("Error in your list-2D")
        t_lst = []
        return t_lst
    except Exception as err:
        print("Error ->", err)
        t_lst = []
        return t_lst
