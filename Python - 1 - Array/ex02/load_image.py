from pathlib import Path
import imageio as iio
import sys


sys.tracebacklimit = 0


def ft_load(path: str) -> list:
    """Function that loads an image from a file into a numpy array."""

    if (not Path(path).exists()):
        raise "File not found"
    if (not Path(path).is_file()):
        raise "Path is not a file"
    if (not Path(path).suffix in [".jpg", ".jpeg"]):
        raise "File is not a jpeg"

    img = iio.v3.imread(path)
    print(f"The shape of the image is: {img.shape}")

    return img
