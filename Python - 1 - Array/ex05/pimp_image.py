from matplotlib import pyplot as plt
import numpy as np


def display_image(img):
    """Displays the image."""
    plt.imshow(img, cmap="gray")
    plt.show()


def ft_invert(array) -> list:
    """Inverts the color of the image received."""
    img = np.array(array)
    img = 255 - img
    return img


def ft_red(array) -> list:
    """Sets the color of the image receuved to red."""
    img = np.array(array)
    img[:, :, 1] = 0
    img[:, :, 2] = 0
    return img


def ft_green(array) -> list:
    """Sets the color of the image received to green."""
    img = np.array(array)
    img[:, :, 0] = 0
    img[:, :, 2] = 0
    return img


def ft_blue(array) -> list:
    """Sets the color of the image received to blue."""
    img = np.array(array)
    img[:, :, 0] = 0
    img[:, :, 1] = 0
    return img


def ft_grey(array) -> list:
    """Sets the color of the image received to grey."""
    img = np.array(array)
    return img[:, :, 0:1]
