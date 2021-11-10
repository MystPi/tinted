import sys
from .core import tint


def main():
    if len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as file:
            print(tint(file.read()))
    elif len(sys.argv) == 1:
        print(tint(sys.stdin.read()), end='')


if __name__ == '__main__':
    main()