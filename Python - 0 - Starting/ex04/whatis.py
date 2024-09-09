import sys


sys.tracebacklimit = 0


def isOddOrEven(value: str) -> str:
    if (int(value) % 2 == 0):
        return "Even"
    return "Odd"


def isInteger(value: str) -> bool:
    try:
        int(value)
        return True
    except ValueError:
        return False


def main():
    if (len(sys.argv) < 2):
        sys.exit()
    if (len(sys.argv) > 2):
        raise AssertionError("more than one argument is provided")
    if (not isInteger(sys.argv[1])):
        raise AssertionError("argument is not an integer")
    print(f"I'm {isOddOrEven(sys.argv[1])}.")


if __name__ == '__main__':
    main()
