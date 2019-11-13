"""
Problem: https://www.hackerrank.com/challenges/python-string-split-and-join/problem
Max Score: 10
Difficulty: Easy
Author: Ric
Date: Nov 13, 2019
"""

def split_and_join(line):
    # write your code here
    return '-'.join(i for i in line.split(' '))

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)