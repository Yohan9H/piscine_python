import numpy as np
import PIL.Image as Image
import matplotlib.pyplot as plt
import load_image as ld


def ft_zoom():
    """ Load and convert 'animal.jpeg' to grayscale, crop a zoomed region,
    print its shape and data, then display it.

    Prints errors if loading or processing fails.
    """
    try:
        ld.ft_load("animal.jpeg")
        img = Image.open("animal.jpeg").convert("L")
        arr = np.array(img)
        zoomed = arr[100:500, 400:800]
        zoomed_1 = np.expand_dims(zoomed, axis=-1)
        print("New shape after slicing:", zoomed_1.shape, "or", zoomed.shape)
        print(zoomed)
        plt.imshow(zoomed, cmap="gray")
        plt.show()

    except Exception as err:
        print("Error ->", err)


if __name__ == "__main__":
    ft_zoom()
