"""
Problem: https://www.hackerrank.com/challenges/py-set-union/problem
Max Score: 10
Difficulty: Easy
Author: Ric
Date: Nov 13, 2019
"""



# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input()
n_set = set(input().split())
b = input()
b_set = set(input().split())
# print(n_set)
# print(b_set)

new_set = n_set.union(b_set)
print(len(new_set))
