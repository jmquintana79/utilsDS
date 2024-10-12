# -*- coding: utf-8 -*-
# @Author: Juan Quintana
# @Date:   2024-10-12 01:06:55
# @Last Modified by:   Juan Quintana
# @Last Modified time: 2024-10-12 13:52:45
"""
Ejemplo de prueba para la automatizacion del code styling.
"""


def my_function(x: int) -> tuple[float, int]:
    """my_function It is my function for testing.

    Arguments:
        x {int} -- Some integer to be divided by 34.

    Returns:
        float -- Division.
    """
    # return
    return (x / 34.0, x)


def function_without_using() -> None:
    """function_without_using Function to not be used."""
    print("no voy a ser usada.")


def greeting(name: str) -> str:
    """greeting Gretting function to test mypy

    Arguments:
        name {str} -- Name

    Returns:
        str -- Combine hello "name"
    """
    # return
    return "Hello " + name


def main() -> None:
    """main Main function."""
    print("Hello, World!")
    y = my_function(56)
    print(y)
    # print("It is", y + 1)
    # greeting(3)         # Argument 1 to "greeting" has
    #                       incompatible type "int"; expected "str"
    # greeting(b'Alice')  # Argument 1 to "greeting" has incompatible
    #                       type "bytes"; expected "str"
    greeting("World!")  # No error


if __name__ == "__main__":
    main()
