"""
Problem: https://www.hackerrank.com/challenges/python-loops/problem
Max Score: 5
Difficulty: Easy
Author: Ric
Date: Nov 13, 2019

"""


if __name__ == '__main__':
    n = int(input())
    flag = 0
    while flag < n:
        print(flag**2)
        flag += 1 