# import matplotlib.pyplot as plt
import numpy as np


def ft_invert(array) -> np.ndarray:
    """Inverts the color of the image received."""
    try:
        if not isinstance(array, np.ndarray):
            arr = np.array(array)
        else:
            arr = array
        arr_invert = 255 - arr
        # plt.imshow(arr_invert)
        # plt.show()
        return arr_invert
    except Exception as err:
        print("Error ->", err)


def ft_red(array) -> np.ndarray:
    """
    Removes the green and blue channels from an RGB image,
    leaving only the red channel.

    Args:
        array (np.ndarray or array-like): A 3D array representing an RGB image,
            typically with shape (height, width, 3).

    Returns:
        np.ndarray: A copy of the input image where the green and blue channels
            have been set to zero, leaving only the red channel visible.

    Raises:
        Exception: If an error occurs during the processing.
    """
    try:
        if not isinstance(array, np.ndarray):
            arr = np.array(array)
        else:
            arr = array
        arr_cpy = arr.copy()
        arr_cpy[:, :, 1] = arr_cpy[:, :, 1] * 0
        arr_cpy[:, :, 2] = arr_cpy[:, :, 2] * 0
        arr_red = arr_cpy
        # plt.imshow(arr_red)
        # plt.show()
        return arr_red
    except Exception as err:
        print("Error ->", err)


def ft_green(array) -> np.ndarray:
    """
    Removes the red and blue channels from an RGB image,
    leaving only the green channel.

    Args:
        array (np.ndarray or array-like): A 3D array representing an RGB image,
            typically with shape (height, width, 3).

    Returns:
        np.ndarray: A copy of the input image where the red and blue channels
            have been set to zero, leaving only the green channel visible.

    Raises:
        Exception: If an error occurs during the processing.
    """
    try:
        if not isinstance(array, np.ndarray):
            arr = np.array(array)
        else:
            arr = array
        arr_cpy = arr.copy()
        arr_cpy[:, :, 0] = arr_cpy[:, :, 0] - arr_cpy[:, :, 0]
        arr_cpy[:, :, 2] = arr_cpy[:, :, 2] - arr_cpy[:, :, 2]
        arr_green = arr_cpy
        # plt.imshow(arr_green)
        # plt.show()
        return arr_green
    except Exception as err:
        print("Error ->", err)


def ft_blue(array) -> np.ndarray:
    """
    Removes the red and green channels from an RGB image,
    leaving only the blue channel.

    Args:
        array (np.ndarray or array-like): A 3D array representing an RGB image,
            typically with shape (height, width, 3).

    Returns:
        np.ndarray: A copy of the input image where the red and green channels
            have been set to zero, leaving only the blue channel visible.

    Raises:
        Exception: If an error occurs during the processing.
    """
    try:
        if not isinstance(array, np.ndarray):
            arr = np.array(array)
        else:
            arr = array
        arr_cpy = arr.copy()
        arr_cpy[:, :, 0] = 0
        arr_cpy[:, :, 1] = 0
        arr_blue = arr_cpy
        # plt.imshow(arr_blue)
        # plt.show()
        return arr_blue
    except Exception as err:
        print("Error ->", err)


def ft_grey(array) -> np.ndarray:
    """
    Converts an RGB image to grayscale by averaging the red,
    green, and blue channels.

    Args:
        array (np.ndarray or array-like): A 3D array representing an RGB image,
            typically with shape (height, width, 3).

    Returns:
        np.ndarray: A grayscale version of the input image,
        where all three channels (R, G, B) have been set to
        the same average intensity value per pixel.

    Raises:
        Exception: If an error occurs during the processing.
    """
    try:
        if not isinstance(array, np.ndarray):
            arr = np.array(array)
        else:
            arr = array
        arr_grey = arr.copy()
        grey = arr_grey.mean(axis=2)
        arr_grey[:, :, 0] = grey
        arr_grey[:, :, 1] = grey
        arr_grey[:, :, 2] = grey
        # plt.imshow(arr_grey)
        # plt.show()
        return arr_grey
    except Exception as err:
        print("Error ->", err)
