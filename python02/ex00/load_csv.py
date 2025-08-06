import pandas as pd


def load(path: str) -> pd.DataFrame:
    """Load a dataset from a CSV file.

    Args:
        path (str): Path to the CSV file.

    Raises:
        AssertionError: If the provided path is not a string.

    Returns:
        pd.DataFrame: Loaded dataset as a DataFrame,
        or None if an error occurs.
    """
    try:
        if not isinstance(path, str):
            raise AssertionError
        data = pd.read_csv(path)
        print("Loading dataset of dimensions", data.shape)
        return data
    except Exception as err:
        print("Error ->", err)
        return None
