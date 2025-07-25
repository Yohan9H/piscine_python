import numpy as np

Nblist = list[int | float]


def give_bmi(height: Nblist, weight: Nblist) -> Nblist:
    """
    Computes the Body Mass Index (BMI) for each individual given
    their height and weight.

    Args:
        height (Nblist): A list of heights in meters (float or int).
        weight (Nblist): A list of weights in kilograms (float or int).

    Raises:
        AssertionError: If the lists are not the same length.
        AssertionError: If height or weight contains non-numeric values.
        AssertionError: If height or weight contains boolean values.

    Returns:
        Nblist: A list of BMI values corresponding to each individual.
    """
    try:
        if len(height) != len(weight):
            raise AssertionError
        h_array = np.array(height)
        w_array = np.array(weight)
        if np.issubdtype(h_array.dtype, np.number) is False:
            raise AssertionError
        if np.issubdtype(w_array.dtype, np.number) is False:
            raise AssertionError
        if h_array.dtype == np.bool_ or w_array.dtype == np.bool_:
            raise AssertionError
        res = w_array / (h_array ** 2)
        return res.tolist()
    except Exception as err:
        print(f"Error {err}")


def apply_limit(bmi: Nblist, limit: int) -> list[bool]:
    """
    Compares each BMI value to a given limit and returns
    a list of boolean values.

    Args:
        bmi (Nblist): A list of BMI values (float or int).
        limit (int): The threshold above which BMI is considered too high.

    Raises:
        AssertionError: If BMI contains non-numeric values.
        AssertionError: If BMI contains boolean values.
        AssertionError: If limit is not an integer.

    Returns:
        list[bool]: A list of booleans indicating whether
        each BMI exceeds the limit.
    """
    try:
        bmi_array = np.array(bmi)
        if np.issubdtype(bmi_array.dtype, np.number) is False:
            raise AssertionError
        if bmi_array.dtype == np.bool_:
            raise AssertionError
        if type(limit) is not int:
            raise AssertionError
        res = bmi_array > limit
        return res.tolist()
    except Exception as err:
        print("Error ", err)
