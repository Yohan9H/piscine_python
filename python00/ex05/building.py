import sys as sys


def main():
    """Counts and displays the number of uppercase letters, lowercase letters,
    digits, spaces, and punctuation characters in a given string.

    If no argument is passed, the program prompts the user for input.

    Raises:
        AssertionError: if more one arguments
    """
    try:
        count = 0
        if len(sys.argv) == 1:
            str_input = input("What is the text to count?\n")
            count = 1
        else:
            str_input = sys.argv[1]

        if len(sys.argv) > 2:
            raise AssertionError

        nb_uppercase = sum(1 for c in str_input if c.isupper())
        nb_lowercase = sum(1 for c in str_input if c.islower())
        nb_space = sum(1 for c in str_input if c.isspace())
        nb_digit = sum(1 for c in str_input if c.isdigit())
        nb_punc = sum(1 for c in str_input
                      if not c.isalnum() and not c.isspace())
        if count == 1:
            nb_space += 1

        print("The text contains", len(str_input) + count, "characters:")
        print(nb_uppercase, "upper letters")
        print(nb_lowercase, "lower letters")
        print(nb_punc, "punctuation marks")
        print(nb_space, "spaces")
        print(nb_digit, "digits")

    except AssertionError:
        print("AssertionError: Invalid arguments.")
        return
    except ValueError:
        print("-- Error --")
        return
    except EOFError:
        return
    except KeyboardInterrupt:
        return


if __name__ == "__main__":
    main()
