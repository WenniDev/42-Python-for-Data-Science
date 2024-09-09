import sys


sys.tracebacklimit = 0


def is_all_type_of_list_good(lst: list, type) -> bool:
    """Check if all elements in a list are of a certain type"""

    return all(isinstance(i, type) for i in lst)


def calculate_bmi(height: int | float, weight: int | float) -> int | float:
    """Calculate the BMI of a person"""

    if (height <= 0):
        assert [], "height must be greater than 0"
    return weight / (height * height)


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """Calculate the BMI of a list of people"""

    if (not len(height) == len(weight)):
        assert [], "height and weight are not the same size"
    if (not is_all_type_of_list_good(height, int | float)):
        assert [], "height is not a list of int or float"
    if (not is_all_type_of_list_good(weight, int | float)):
        assert [], "weight is not a list of int or float"
    return [calculate_bmi(height[i], weight[i]) for i in range(len(height))]


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Apply a limit to a list of BMI"""

    if (not is_all_type_of_list_good(bmi, int | float)):
        assert [], "bmi is not a list of int or float"
    if (limit <= 0):
        assert [], "limit must be greater than 0"
    return [True if i > limit else False for i in bmi]
