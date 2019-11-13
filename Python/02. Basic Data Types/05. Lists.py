"""
Problem: https://www.hackerrank.com/challenges/python-lists/problem
Max Score: 10
Difficulty: Easy
Author: Ric
Date: Nov 13, 2019
"""

if __name__ == '__main__':
    N = int(input())
    list = []
    for i in range(N):
        command = input().split()
        action = command[0]
        if action == "print":
            print(list)
        elif action == "sort":
            list.sort()
        elif action == "reverse":
            list.reverse()
        elif action == "pop":
            list.pop()
        elif action == "remove":
            CV1 = command[1]
            list.remove(int(CV1))
        elif action == "append":
            CV1 = command[1]
            list.append(int(CV1))
        elif action == "insert":
            CV1, CV2 = command[1], command[2]
            list.insert(int(CV1), int(CV2))
