"""
Problem: https://www.hackerrank.com/challenges/no-idea/problem
Max Score: 50
Difficulty: Medium
Author: Ric
Date: Nov 13, 2019
"""


# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = input().split()
arr = list(map(int, input().split()))
setA = set(input().split())
setB = set(input().split())
# print(n)
# print(m)
# print(arr)
# print(setA)
# print(setB)

happiness = 0
for i in arr:
    if str(i) in setA:
        happiness += 1
    elif str(i) in setB:
        happiness -= 1
    else:
        continue

print(happiness)
