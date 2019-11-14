"""
Problem: https://www.hackerrank.com/challenges/zipped/problem
Max Score: 10
Difficulty: Easy
Author: Ric
Date: Nov 14, 2019

"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
student, subject = map(int, input().split())

scores = list()

scores = [list(map(float, input().split())) for i in range(subject)]

scores_by_student = zip(*scores)

# print(list(scores_by_student))

average_by_student = [sum(i) / subject for i in list(scores_by_student)]

for i in average_by_student:
    print(i)