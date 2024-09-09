import math


def NULL_not_found(object: any) -> int:
    type_null = {
        (None, type(None)): "Nothing",
        (0, type(0)): "Zero",
        (math.nan, type(math.nan)): "Cheese",
        ('', type('')): "Empty",
        (False, type(False)): "Fake"
    }

    if (isinstance(object, (int, float, complex)) and math.isnan(object)):
        object = math.nan

    object_type = type_null.get((object, type(object)))

    if (not object_type):
        print("Type not Found")
        return 1

    print(f"{object_type}: {object} {type(object)}")
    return 0
