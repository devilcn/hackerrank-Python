"""
Problem: https://www.hackerrank.com/challenges/string-validators/problem
Max Score: 10
Difficulty: Easy
Author: Ric
Date: Nov 13, 2019
"""


if __name__ == '__main__':
    s = input()

  # any() == True if any iterable item is True
  # any() == False if all iterable items are False
    print(any([i.isalnum() for i in s]))
    print(any([i.isalpha() for i in s]))
    print(any([i.isdigit() for i in s]))
    print(any([i.islower() for i in s]))
    print(any([i.isupper() for i in s]))