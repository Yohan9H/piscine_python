import PIL.Image as Image
import numpy as np


def ft_load(path: str) -> np.ndarray:
    """Loads an image from the given path, converts it to RGB format,
    prints its shape, and returns its pixel data as a NumPy array.

    Args:
        path (str): The file path to the image.

    Returns:
        np.array: A NumPy array representing the image in RGB format.

    Raises:
        AssertionError: If the path argument is not a string.
        Exception: If the image cannot be opened or converted.
    """
    try:
        if not isinstance(path, str):
            raise AssertionError
        img = Image.open(path)
        img = img.convert("RGB")
        arr = np.array(img)
        print("The shape of image is:", arr.shape)
        print(arr)
        return arr
    except AssertionError:
        print("Error -> arg is bad type")
    except Exception as err:
        print("Error ->", err)
