"""
Problem: https://www.hackerrank.com/challenges/py-introduction-to-sets/problem
Max Score: 10
Difficulty: Easy
Author: Ric
Date: Nov 13, 2019
"""


def average(arr):
    # your code goes here
    dist_set = set(arr)
    new_list = []
    for i in dist_set:
        new_list.append(i)
    return sum(new_list) / len(dist_set)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)