import pandas as pd


def load(path: str) -> pd.DataFrame:
    try:
        if not isinstance(path, str):
            raise AssertionError
        data = pd.read_csv(path)
        print("Loading dataset of dimensions", data.shape)
        return data
    except Exception as err:
        print("Error ->", err)
        return None
