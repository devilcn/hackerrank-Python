"""
Problem: https://www.hackerrank.com/challenges/write-a-function/problem
Max Score: 10
Difficulty: Medium
Author: Ric
Date: Nov 13, 2019

"""


def is_leap(year):
    leap = False
    
    # Write your logic here
    if year % 4 == 0 and year % 100 != 0:
        leap = True
    elif year % 400 == 0:
        leap = True
    
    return leap