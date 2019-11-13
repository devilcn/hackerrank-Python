"""
Problem: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
Max Score: 10
Difficulty: Easy
Author: Ric
Date: Nov 13, 2019
"""

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    # new_arr = []
    # for i in range(1, n+1):
    #     if i != max(arr):
    #         new_arr.append(i)
    # print(max(new_arr))
    print(sorted(list(set(arr)))[-2])