"""
Problem: https://www.hackerrank.com/challenges/finding-the-percentage/problem
Max Score: 10
Difficulty: Easy
Author: Ric
Date: Nov 13, 2019
"""

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        # print(name)
        # print(line)
        # scores = list(map(float, line))
        aveScore = sum(list((map(float, line)))) / 3
        student_marks[name] = aveScore
    query_name = input()
    print('%.2f' % student_marks[query_name])