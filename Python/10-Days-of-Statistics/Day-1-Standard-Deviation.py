#!/bin/python3

import math
import os
import random
import re
import sys
from decimal import Decimal

#
# Complete the 'stdDev' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#
def output_custimization(x):  # output custimization
    x_out = Decimal(x).quantize(Decimal("0.0"))
    return x_out

def mean_cal(array_input,N):  # mean cal
    sum_temp = 0
    for i in array_input:
        sum_temp = int(i)+sum_temp
    mean = sum_temp/N
    return mean

def stdDev(arr,n):
    # Print your answers to 1 decimal place within this function
    mean = mean_cal(arr,n)
    sum_temp = 0
    for i in arr:
        sum_temp = (i - mean)**2 + sum_temp
    result = output_custimization((sum_temp / n)**0.5)
    print(result)

if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    stdDev(vals,n)
