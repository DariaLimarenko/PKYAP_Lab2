import colorama
from colorama import Fore, Style

from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square


def main():
    colorama.init(autoreset=True)

    N = 15

    rectangle = Rectangle(N, N, "синий")
    circle = Circle(N, "зелёный")
    square = Square(N, "красный")

    print("Лабораторная работа №2")
    print("Вариант: {}".format(N))
    print()

    print(Fore.BLUE + repr(rectangle) + Style.RESET_ALL)
    print(Fore.GREEN + repr(circle) + Style.RESET_ALL)
    print(Fore.RED + repr(square) + Style.RESET_ALL)


if __name__ == "__main__":
    main()
