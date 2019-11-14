"""
Problem: https://www.hackerrank.com/challenges/input/problem
Max Score: 20
Difficulty: Easy
Author: Ric
Date: Nov 14, 2019

"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

x, k = map(int, input().split())

command = eval(input())
# print(type(command))
Flag = False
if command == k:
    Flag = True
print(Flag)