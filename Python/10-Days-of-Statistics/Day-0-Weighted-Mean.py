#!/bin/python3

import math
import os
import random
import re
import sys
from decimal import Decimal

#
# Complete the 'weightedMean' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY X
#  2. INTEGER_ARRAY W
#
def output_custimization(x):  # output custimization
    x_out = Decimal(x).quantize(Decimal("0.0"))
    return x_out

def weightedMean(X, W):
    sum_W = 0
    sum_cross = 0
    for i in W:
        sum_W = int(i)+sum_W
    for i in range(0,len(W)):
        sum_cross = int(X[i]*W[i]) + sum_cross
    ori_result = sum_cross/sum_W    
    result = output_custimization(ori_result)
    print(result)
    
if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    weights = list(map(int, input().rstrip().split()))

    weightedMean(vals, weights)
