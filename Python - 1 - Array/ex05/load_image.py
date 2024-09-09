from pathlib import Path
import imageio as iio


def ft_load(path: str) -> list:
    """Function that loads an image from a file into a numpy array."""

    if (not Path(path).exists()):
        assert None, "File not found"
    if (not Path(path).is_file()):
        assert None, "Path is not a file"
    if (not Path(path).suffix in [".jpg", ".jpeg"]):
        assert None, "File is not a jpeg"

    img = iio.v3.imread(path)
    return img
