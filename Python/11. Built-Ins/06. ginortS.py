"""
Problem: https://www.hackerrank.com/challenges/ginorts/problem
Max Score: 40
Difficulty: Medium
Author: Ric
Date: Nov 15, 2019

"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
str_ori = input()
order = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1357902468'
sorted_Str = sorted(str_ori, key=order.index)
print(*sorted_Str, sep='')