"""
Problem: https://www.hackerrank.com/challenges/py-check-subset/problem
Max Score: 10
Difficulty: Easy
Author: Ric
Date: Nov 13, 2019
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())
for i in range(T):
    num_A, set_A = int(input()), set(map(int, input().split()))
    num_B, set_B = int(input()), set(map(int, input().split()))
    print(set_A.issubset(set_B))

