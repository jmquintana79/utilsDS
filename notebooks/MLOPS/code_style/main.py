# -*- coding: utf-8 -*-
# @Author: Juan Quintana
# @Date:   2024-10-12 01:06:55
# @Last Modified by:   Juan Quintana
# @Last Modified time: 2024-10-12 02:16:53
"""
## black
Code style formatting automatically.
https://black.readthedocs.io/en/stable/
> black main.py

## flake8
Static code analysis, just for warning, not repearing automatically.
https://flake8.pycqa.org/en/latest/index.html#quickstart
> flake8 main.py

## pylint
Static code analysis to force coding stardards and detect errors.
For me, it is very similar than flake8 with maybe some different checks.
I like a lot and finally return a rate.
https://github.com/pylint-dev/pylint
> pylint main.py

## mypy
Mypy is a static type checker.
It is not working for me. Always return a success message:
> mypy main.py
However, forzing a strict mode, working more strongly:
> mypy --strict main.py
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
