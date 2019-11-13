"""
Problem: https://www.hackerrank.com/challenges/find-a-string/problem
Max Score: 10
Difficulty: Easy
Author: Ric
Date: Nov 13, 2019
"""


def count_substring(string, sub_string):
    occ = 0
    lenth_A = len(string)
    lenth_B = len(sub_string)
    for i in range(lenth_A - lenth_B + 1):
        if string[i: i + len(sub_string)] == sub_string:
            occ += 1
    return occ
    

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)