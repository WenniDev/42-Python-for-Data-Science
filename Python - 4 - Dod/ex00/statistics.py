from typing import Any


def get_mean(*args: Any) -> float:
    assert len(args) > 0, ValueError()
    return sum(args) / len(args)


def get_median(*args: Any) -> float:
    args = sorted(args)
    if len(args) % 2 == 0:
        return (args[len(args) // 2 - 1] + args[len(args) // 2]) / 2
    else:
        return args[len(args) // 2]


def get_quartile(*args: Any) -> list[float]:
    args = sorted(args)
    return [float(args[1]), float(args[-2])]


def get_std(*args: Any) -> float:
    return (sum(args) / len(args)) ** 0.5


def get_var(*args: Any) -> float:
    return sum(args) / len(args) ** 0.5


def exec_stat(values: Any, *args: Any) -> float:
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
        if values in func_stat:
            print(f"{values} : {func_stat[values](*args)}")


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    for value in kwargs.values():
        exec_stat(value, *args)
