"""
Problem: https://www.hackerrank.com/challenges/python-sort-sort/problem
Max Score: 30
Difficulty: Medium
Author: Ric
Date: Nov 15, 2019

"""

#!/bin/python3

import math
import os
import random
import re
import sys


def locate_index(elem):
    return elem[k]
    

if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []


    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    
    k = int(input())

    for i in range(n):
        arr.sort(key=locate_index)

    for i in arr:
        print(*i, sep=" ")