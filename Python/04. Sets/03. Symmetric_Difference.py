"""
Problem: https://www.hackerrank.com/challenges/symmetric-difference/problem
Max Score: 10
Difficulty: Easy
Author: Ric
Date: Nov 13, 2019
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
M = input()
M_set = set(list(map(int, input().split())))
N = input()
N_set = set(list(map(int, input().split())))

symmetric_diff = []
for i in range(max(len(M), len(N))):
    new_set = M_set.difference(N_set).union(N_set.difference(M_set))
     # Only in M not in N & only in N not in M
sorted_list = sorted(list(new_set))
for i in sorted_list:
    print(i)
