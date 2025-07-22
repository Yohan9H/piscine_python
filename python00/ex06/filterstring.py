import sys as sys
from ft_filter import ft_filter


def verif_string(string: str):
    punc = "!#$%&'()*+,-./:;<=>?@[\\]^_{|}~"
    for c in string:
        if c in punc or not c.isprintable():
            return False
    return True


def filterstring(string: str, nb: int):
    if verif_string(string) is False:
        raise AssertionError
    list_string = string.split()
    res = ft_filter(lambda x: len(x) > nb, list_string)
    print(*res)


def main():
    try:
        if len(sys.argv) > 3 or len(sys.argv) == 1:
            raise AssertionError
        av1 = str(sys.argv[1])
        av2 = int(sys.argv[2])
        filterstring(av1, av2)
    except Exception as err:
        print("AssertionError: the arguments are bad --", err)
        return


if __name__ == "__main__":
    main()
