import sys
import string


sys.tracebacklimit = 0


def main():
    if (len(sys.argv) > 2):
        raise AssertionError("only one argument is required")
    if (len(sys.argv) < 2):
        sentence = input("What is the text to count?\n")
    else:
        sentence = sys.argv[1]

    def check_count(check):
        """ Count the number of characters in a sentence
        that satisfy a condition """
        return len(list(filter(check, sentence)))

    print(f"The text contains {len(sentence)} characters:")
    print(f"{check_count(lambda c: c.isupper())} upper letters")
    print(f"{check_count(lambda c: c.islower())} lower letters")
    print(f"{check_count(lambda c: c in string.punctuation)} \
punctuation marks")
    print(f"{check_count(lambda c: c.isspace())} spaces")
    print(f"{check_count(lambda c: c.isdigit())} digits")
    return 0


if __name__ == '__main__':
    main()
