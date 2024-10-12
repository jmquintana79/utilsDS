# -*- coding: utf-8 -*-
# @Author: Juan Quintana
# @Date:   2024-10-12 20:16:16
# @Last Modified by:   Juan Quintana
# @Last Modified time: 2024-10-12 20:49:39

import sys
sys.path.append("../../")
import pytest
from src.module1.module11 import func1_mod11, func2_mod11, func3_mod11
import random


@pytest.fixture
def get_random_float():
    return random.random()


def test_func1_mod11_in_normal_operation(get_random_float):
    x = get_random_float
    assert func1_mod11(x, 2.) == x + 2.
    assert func1_mod11(1., 0) == 1.


def test_func2_mod11_in_normal_operation_and_with_uncontroled_error():
    assert func2_mod11(4., 2.) == 2.
    with pytest.raises(Exception): ## case of an unknowledged exception
        func2_mod11(5, 0)


def test_func3_mod11_in_normal_operation_and_with_controled_error():
    assert func3_mod11(3., 2.) == 1.5
    with pytest.raises(ValueError):  ## case of an knowledged exception (ValueError)
        func3_mod11(5, 0)