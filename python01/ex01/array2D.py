import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    try:
        ## Faire les verifs de type size blablabla
        t_lst = np.array(family)
        print("My shape is :", t_lst.shape)
        trunc = t_lst[start:end]
        print("My new shape is :", trunc.shape)
        return trunc.tolist()
    except Exception as err:
        print("Error ->", err)
