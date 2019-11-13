"""
Problem: https://www.hackerrank.com/challenges/py-if-else/problem
Max Score: 10
Difficulty: Easy
Author: Ric
Date: Nov 11, 2019

"""


if __name__ == "__main__":
    n = int(input().strip())
    if n % 2 != 0:
        print("Weird")
    elif 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    else:
        print("Not Weird")