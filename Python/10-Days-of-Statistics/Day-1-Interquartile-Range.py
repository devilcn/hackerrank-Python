#!/bin/python3

import math
import os
import random
import re
import sys
from decimal import Decimal

#
# Complete the 'interQuartile' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY freqs
#
def output_custimization(x):  # output custimization
    x_out = Decimal(x).quantize(Decimal("0.0"))
    return x_out

def median_cal(array_input):  # median cal
    if len(array_input)%2 == 1:
        if len(array_input) ==1:
            result = array_input[0]
        else:
            result = array_input[len(array_input)//2]
    else:
        m,n = len(array_input) // 2 - 1, len(array_input) // 2
        result = (int(array_input[m]) + int(array_input[n])) / 2
    return result

def quartiles(arr):
    m = int(len(arr)/2)
    if len(arr) % 2 == 0:
        lower_qt_arr = arr[0:m]
        mid_qt_arr = arr[m-1:m+1]
        higher_qt_arr = arr[m:] 
    else:
        lower_qt_arr = arr[0:m]
        mid_qt_arr = arr[m:m+1]
        higher_qt_arr = arr[m+1:]
    a = median_cal(lower_qt_arr)
    b = median_cal(mid_qt_arr)
    c = median_cal(higher_qt_arr)
    return a,b,c  

def new_arr(values,freqs):
    new_arr_list=[]
    for i in range(len(values)):
            for j in range(freqs[i]):
                new_arr_list.append(values[i])
    new_arr_list.sort(key=lambda x: (len(str(x)), x ))
    return new_arr_list
    
def interQuartile(values, freqs):
    # Print your answer to 1 decimal place within this function
    new_arr_list = new_arr(values, freqs)
    Q1,Q2,Q3 = quartiles(new_arr_list)
    result = Q3 - Q1
    return output_custimization(result)

if __name__ == '__main__':
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))

    print(interQuartile(val, freq))
