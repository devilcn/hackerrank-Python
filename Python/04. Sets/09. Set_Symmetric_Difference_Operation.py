"""
Problem: https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem
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
new_set = n_set.symmetric_difference(b_set)
print(len(new_set))