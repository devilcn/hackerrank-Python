"""
Problem: https://www.hackerrank.com/challenges/py-check-strict-superset/problem
Max Score: 10
Difficulty: Easy
Author: Ric
Date: Nov 13, 2019
"""



# # Enter your code here. Read input from STDIN. Print output to STDOUT
# set_A = set(map(int, input().split()))

# print(all(set_A > set(input().split()) for _ in range(int(input()))))



A = set(map(int, input().split()))
N = int(input())

isstrictsuperset = True

for i in range(N):
    s = set(map(int, input().split()))
    if not s.issubset(A):
        isstrictsuperset = False
    if len(s) >= len(A):
        isstrictsuperset = False

print(isstrictsuperset)
