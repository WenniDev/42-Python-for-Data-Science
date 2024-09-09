from load_image import ft_load
from matplotlib import pyplot as plt
import sys


sys.tracebacklimit = 0


def set_grayscale(img):
    """Sets the image to grayscale."""
    return img[:, :, 0:1]


def zoom_image_by(img, begin=(0, 0), size=(400, 400)):
    """Zooms the image by a given percentage."""
    return img[begin[1]:size[1] + begin[1], begin[0]:size[0] + begin[0]]


def main():
    img = ft_load("./animal.jpeg")
    print(f"The shape of the image is: {img.shape}")
    print(img)

    img = zoom_image_by(img, (400, 150), (400, 400))
    img = set_grayscale(img)

    print(f"The shape after slicing: {img.shape[:2]}")
    print(img)

    plt.imshow(img, cmap="gray")
    plt.show()


if (__name__ == "__main__"):
    main()
