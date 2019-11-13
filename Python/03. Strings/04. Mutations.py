"""
Problem: https://www.hackerrank.com/challenges/python-mutations/problem
Max Score: 10
Difficulty: Easy
Author: Ric
Date: Nov 13, 2019
"""


def mutate_string(string, position, character):
    # l = list(s)
    # l[int(i)] = c
    # l_s = ''.join(l)
    # return l_s

    l_s = s[:int(i)] + c + s[(int(i)+1):]
    return l_s


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)