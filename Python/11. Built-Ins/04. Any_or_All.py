"""
Problem: https://www.hackerrank.com/challenges/any-or-all/problem
Max Score: 20
Difficulty: Easy
Author: Ric
Date: Nov 14, 2019

"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
num_of_int = int(input())
list_of_int = list(map(int, input().split(" ")))
print(all(i > 0 for i in list_of_int) and any(str(i) == str(i)[::-1] for i in list_of_int))