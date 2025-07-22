import sys as sys


def sos():
    """Converts a command-line argument string to Morse code and prints it.

    Checks that exactly one argument is provided,
    verifies the string contains no disallowed special characters,
    then translates each alphanumeric character or space to Morse code.

    Raises:
        AssertionError: If the number of arguments is not exactly one.
        AssertionError: If the input string contains special
        or non-printable characters.
    """
    NESTED_MORSE = {
        " ": "/ ",
        "A": ".- ",
        "B": "-... ",
        "C": "-.-. ",
        "D": "-.. ",
        "E": ". ",
        "F": "..-. ",
        "G": "--. ",
        "H": ".... ",
        "I": ".. ",
        "J": ".--- ",
        "K": "-.- ",
        "L": ".-.. ",
        "M": "-- ",
        "N": "-. ",
        "O": "--- ",
        "P": ".--. ",
        "Q": "--.- ",
        "R": ".-. ",
        "S": "... ",
        "T": "- ",
        "U": "..- ",
        "V": "...- ",
        "W": ".-- ",
        "X": "-..- ",
        "Y": "-.-- ",
        "Z": "--.. ",
        "0": "----- ",
        "1": ".---- ",
        "2": "..--- ",
        "3": "...-- ",
        "4": "....- ",
        "5": "..... ",
        "6": "-.... ",
        "7": "--... ",
        "8": "---.. ",
        "9": "----. "
    }
    try:
        if len(sys.argv) != 2:
            raise AssertionError

        string = str(sys.argv[1]).upper()
        for c in string:
            if c in "!#$%&'()*+,-./:;<=>?@[\\]^_{|}~":
                raise AssertionError

        res = ""
        for c in string:
            if c in NESTED_MORSE:
                res += NESTED_MORSE.get(c)

        if res.endswith(" "):
            res = res.rstrip()
        print(res)

    except AssertionError:
        print("AssertionError: the aguments are bad")
    except Exception as err:
        print("Error", err)


if __name__ == "__main__":
    sos()
