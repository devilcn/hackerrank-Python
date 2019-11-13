"""
Problem: https://www.hackerrank.com/challenges/whats-your-name/problem
Max Score: 10
Difficulty: Easy
Author: Ric
Date: Nov 13, 2019
"""

def print_full_name(a, b):
    print("Hello %s %s! You just delved into python." %(first_name, last_name))

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)