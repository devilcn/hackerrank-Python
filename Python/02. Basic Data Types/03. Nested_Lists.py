"""
Problem: https://www.hackerrank.com/challenges/nested-list/problem
Max Score: 10
Difficulty: Easy
Author: Ric
Date: Nov 13, 2019
"""

def secondLow(classList):
    secondLowScore = sorted(set(m[1] for m in classList))[1]
    result = sorted([m[0] for m in classList if m[1] == secondLowScore])
    return result

n = int(input())
classList = []
for i in range(n):
    classList.append([str(input()), float(input())])
# print(classList)
print('\n'.join(secondLow(classList)))