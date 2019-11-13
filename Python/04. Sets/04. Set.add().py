"""
Problem: https://www.hackerrank.com/challenges/py-set-add/problem
Max Score: 10
Difficulty: Easy
Author: Ric
Date: Nov 13, 2019
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
s = set('')
for i in range(n):
    s.add(input())
    
total_num = len(s)
print(total_num)