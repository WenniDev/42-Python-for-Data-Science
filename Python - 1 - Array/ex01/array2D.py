import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """Slice a list of lists"""

    if (start > len(np.array(family).shape)):
        raise ValueError('Negative values are not allowed')

    print(f'My shape is : {np.array(family).shape}')
    x = slice(start, end)
    print(f'My new shape is : {np.array(family[x]).shape}')

    return family[x]
