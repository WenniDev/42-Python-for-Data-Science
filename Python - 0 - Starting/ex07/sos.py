import sys


sys.tracebacklimit = 0


def check_args(args: list) -> int:
    """
check_args(args: list) -> int
    """

    if (len(args) != 2):
        return 1
    if (filter(lambda letter: letter.isalnum() or
               letter.isspace(), args[1]) == ''):
        return 1
    return 0


def to_morse(word: str) -> str:
    """
to_morse(word: str) -> str
    """
    NESTED_MORSE = {
        'A': '.-',     'B': '-...',   'C': '-.-.',    'D': '-..',
        'E': '.',      'F': '..-.',   'G': '--.',     'H': '....',
        'I': '..',     'J': '.---',   'K': '-.-',     'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',     'P': '.--.',
        'Q': '--.-',   'R': '.-.',    'S': '...',     'T': '-',
        'U': '..-',    'V': '...-',   'W': '.--',     'X': '-..-',
        'Y': '-.--',   'Z': '--..',   '1': '.----',   '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',   '6': '-....',
        '7': '--...',  '8': '---..',  '9': '----.',   '0': '-----',
        ' ': '/'
    }
    result = map(str, [NESTED_MORSE[letter.upper()] for letter in word])
    return ' '.join(result)


def main():
    if (check_args(sys.argv)):
        raise AssertionError("the arguments are bad")
    print(to_morse(sys.argv[1]))
    return 0


if __name__ == '__main__':
    main()
