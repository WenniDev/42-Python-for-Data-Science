import sys
from ft_filter import ft_filter


sys.tracebacklimit = 0


def check_args(args: list) -> int:
    """
check_args(args: list) -> int
    """

    if (len(args) != 3):
        return 1
    if (not args[2].isdigit()):
        return 1
    return 0


def main():
    if (check_args(sys.argv)):
        raise AssertionError("the arguments are bad")
    words = sys.argv[1].split()
    result = ft_filter(lambda word: len(word) > int(sys.argv[2]), words)
    print(list(result))
    return 0


if __name__ == '__main__':
    main()
