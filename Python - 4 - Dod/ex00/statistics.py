from math import sqrt
from typing import Any


def get_mean(args: tuple) -> float:
    if len(args) == 0:
        raise ValueError("Cannot divide by Zero")
    return sum(args) / len(args)


def get_median(args: tuple) -> float:
    args = sorted(args)
    if len(args) % 2 == 0:
        return (args[len(args) // 2 - 1] + args[len(args) // 2]) / 2
    else:
        return args[len(args) // 2]


def get_quartile(args: tuple) -> list[float]:
    if len(args) < 2:
        raise ValueError("Need at least two values to get the quartile")
    args = sorted(args)
    return [float(args[1]), float(args[-2])]


def get_std(args: tuple) -> float:
    var = get_var(args)
    return sqrt(var)


def get_var(args: tuple) -> float:
    mean = get_mean(args)
    return sum((x - mean) ** 2 for x in args) / len(args)


def exec_stat(values: float, *args: tuple) -> float:
    func_stat = {
        "mean": get_mean,
        "median": get_median,
        "quartile": get_quartile,
        "std": get_std,
        "var": get_var
    }

    if (len(args) <= 0):
        print("ERROR")
    else:
        try:
            if values in func_stat:
                print(f"{values} : {func_stat[values](args)}")
        except ValueError:
            print("ERROR")


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    for value in kwargs.values():
        exec_stat(value, *args)
