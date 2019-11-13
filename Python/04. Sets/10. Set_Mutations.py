"""
Problem: https://www.hackerrank.com/challenges/py-set-mutations/problem
Max Score: 10
Difficulty: Easy
Author: Ric
Date: Nov 13, 2019
"""


# Enter your code here. Read input from STDIN. Print output to STDOUT
num_A = input()
set_A = set(map(int, input().split()))
num_other = input()
for i in range(int(num_other)):
    command = list(input().split())[0]
    temp_set = set(map(int, input().split()))
    if command == "intersection_update":
        set_A.intersection_update(temp_set)
    if command == "update":
        set_A.update(temp_set)
    if command == "symmetric_difference_update":
        set_A.symmetric_difference_update(temp_set)
    if command == "difference_update":
        set_A.difference_update(temp_set)
print(sum(set_A))


# def handler(a):
#     command = input().split()[0]
#     new_set = set(map(int, input().split()))
#     if command == 'intersection_update':
#         a.intersection_update(new_set)
#     if command == 'update':
#         a.update(new_set)
#     if command == 'symmetric_difference_update':
#         a.symmetric_difference_update(new_set)
#     if command == 'difference_update':
#         a.difference_update(new_set)


# _, a = input(), set(map(int, input().split()))
# for i in range(int(input())):
#     handler(a)
# print(sum(a))

