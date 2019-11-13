"""
Problem: https://www.hackerrank.com/challenges/python-print/problem
Max Score: 20
Difficulty: Easy
Author: Ric
Date: Nov 13, 2019

"""

if __name__ == '__main__':
    n = int(input())
    if n >= 1:
        gen_arr = range(1, n+1)
        for i in gen_arr:
            print(i, end='')