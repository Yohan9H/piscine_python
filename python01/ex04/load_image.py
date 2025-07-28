import PIL.Image as Image
import numpy as np


def ft_zoom(path: str):
    """ Load and convert 'animal.jpeg' to grayscale, crop a zoomed region,
    print its shape and data, then display it.

    Prints errors if loading or processing fails.
    """
    try:
        img = Image.open(path).convert("L")
        arr = np.array(img)
        zoomed = arr[100:500, 400:800]
        zoomed_1 = np.expand_dims(zoomed, axis=-1)
        print("The shape of image is:", zoomed_1.shape, "or", zoomed.shape)
        print(zoomed_1)

    except Exception as err:
        print("Error ->", err)