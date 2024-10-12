# -*- coding: utf-8 -*-
# @Author: Juan Quintana
# @Date:   2024-10-12 12:34:10
# @Last Modified by:   Juan Quintana
# @Last Modified time: 2024-10-12 20:30:41
""" 
Este es el primer submodulo del modulo1.
"""


def func1_mod11(x: int, y: float) -> float:
    """func1_mod11 Sum of float numbers.

    Esto es solo un ejemplo.

    Arguments:
        x {int} -- First sum member.
        y {float} -- Second sum member.

    Returns:
        float -- Sum result.
    """
    return float(x) + y

def func2_mod11(x: float, y:float) -> float:
    """Division

    Arguments:
        x {float} -- Numerator      
        y {float} -- Denominator

    Returns:
        float -- Result
    """    
    return x / y


def func3_mod11(x: float, y:float) -> float:
    """Division

    Arguments:
        x {float} -- Numerator      
        y {float} -- Denominator

    Returns:
        float -- Result
    """   
    try:
        return x / y
    except:
        raise ValueError("stop")


def main():
    """main Main function.
    """
    print("Hello, World!")


if __name__ == "__main__":
    main()
