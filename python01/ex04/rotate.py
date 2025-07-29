import matplotlib.pyplot as plt
import PIL.Image as Image
import numpy as np
import load_image as ld


def ft_rotate():
    """ Make zoom inside picture
    """
    try:
        ld.ft_zoom("animal.jpeg")
        img = Image.open("animal.jpeg").convert("L")
        arr = np.array(img)
        zoomed = arr[100:500, 400:800]
        rot = np.zeros((400, 400))
        for i in range(len(zoomed)):
            for j in range(len(zoomed[i])):
                rot[j][i] = zoomed[i][j]
        print("New shape after Transpose:", rot.shape)
        print(rot)
        plt.imshow(rot, cmap="gray")
        plt.show()
    except Exception as err:
        print("Error ->", err)


if __name__ == "__main__":
    ft_rotate()
