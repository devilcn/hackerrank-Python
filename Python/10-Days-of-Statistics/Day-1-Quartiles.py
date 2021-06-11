#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def median_cal(array_input):  # median cal
    if len(array_input)%2 == 1:
        if len(array_input) ==1:
            result = array_input[0]
        else:
            result = array_input[len(array_input)//2]
    else:
        m,n = len(array_input) // 2 - 1, len(array_input) // 2
        print(m,n)
        result = (int(array_input[m]) + int(array_input[n])) / 2
        print(result)
    return int(result)

def quartiles(arr):
    # Write your code here
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
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))
    data.sort(key=lambda x: (len(str(x)), x ))
    res = quartiles(data)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
