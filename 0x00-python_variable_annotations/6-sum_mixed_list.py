#!/usr/bin/env python3
from typing import List, Union

# Function to calculate the sum of a list of integers and floats
def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    return sum(mxd_lst)
