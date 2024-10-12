# -*- coding: utf-8 -*-
# @Author: Juan Quintana
# @Date:   2024-10-12 20:16:31
# @Last Modified by:   Juan Quintana
# @Last Modified time: 2024-10-12 20:39:28

import sys
sys.path.append("../../")
import pytest
from src.module1.module12 import func1_mod21

def test_func1_mod21_in_normal_operation():
    assert func1_mod21(1, 2.) == 3.
    assert func1_mod21(1., 0) == 1.




