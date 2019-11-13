"""
Problem: https://www.hackerrank.com/challenges/python-tuples/problem
Max Score: 10
Difficulty: Easy
Author: Ric
Date: Nov 13, 2019
"""

if __name__ == '__main__':
    n = int(input())
    integer_list = tuple(map(int, input().split()))
    # print(type(integer_list))
    print(hash(integer_list))