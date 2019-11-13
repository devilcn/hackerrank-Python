"""
Problem: https://www.hackerrank.com/challenges/swap-case/problem
Max Score: 10
Difficulty: Easy
Author: Ric
Date: Nov 13, 2019
"""


def swap_case(s):  
    return s.swapcase()


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)