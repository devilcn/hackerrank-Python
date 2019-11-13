"""
Problem: https://www.hackerrank.com/challenges/capitalize/problem
Max Score: 20
Difficulty: Easy
Author: Ric
Date: Nov 13, 2019
"""


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    # return s.title() # This method does not fit for all test cases
    result = ' '.join(i.capitalize() for i in s.split(' '))
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()