#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 06:18:51 2023

@author: mariapasz
"""

def solve_part_one(in_list):
    '''
    Solves part one.
    '''
    result = 0
    div_pos = in_list[1].find('|')
    for row in in_list:
        win_num = row[7:div_pos].split()
        num_have = row[div_pos+1:].split()
        intersection = len(set.intersection(set(win_num), set(num_have)))
        if intersection:
            result += 2**(intersection-1)
    return result

# def _find_intersections_length(in_list):
#     div_pos = in_list[1].find('|')
#     intersection = {}
#     for row_num, row in enumerate(in_list):
#         win_num = row[7:div_pos].split()
#         num_have = row[div_pos+1:].split()
#         intersection[row_num+1] = len(set.intersection(set(win_num), set(num_have)))
#     return intersection
    

def solve_part_two(in_list):
    '''
    Solves part two.
    '''
    new_pile = {_:1 for _ in range(1,len(NUMBERS)+1)}
    div_pos = in_list[1].find('|')
    intersection = {}
    for row_num, row in enumerate(in_list):
        win_num = row[7:div_pos].split()
        num_have = row[div_pos+1:].split()
        intersection[row_num+1] = len(set.intersection(set(win_num), set(num_have)))
    for key, value in intersection.items():
        for _ in range(1,value+1):
            if _ <= len(in_list):
                new_pile[key+_] += new_pile[key]
    return sum(new_pile.values())

with open('input.txt', 'r', encoding="utf-8") as file:
    NUMBERS = file.readlines()

NUMBERS = [x.strip() for x in NUMBERS]

print(solve_part_one(NUMBERS))
print(solve_part_two(NUMBERS))