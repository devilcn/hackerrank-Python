"""
Problem: https://www.hackerrank.com/challenges/py-the-captains-room/problem
Max Score: 10
Difficulty: Easy
Author: Ric
Date: Nov 13, 2019
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
group_size = int(input())
room_list = list(map(int,input().split()))
room_num_type = set(room_list)
cap_num = (sum(room_num_type) * group_size - sum(room_list)) // (group_size -1)
print(cap_num)
