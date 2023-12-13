#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 06:06:16 2023

@author: mariapasz
"""
import collections

def solve_part_one(in_list):
    '''
    Solves part one.
    '''
    reflection_line_row = []
    reflection_line_col = []
    while '' in in_list:
        ind = in_list.index('')
        reflection_line_row.append(_find_reflection_line(in_list[0:ind]))
        reflection_line_col.append(_find_reflection_line(_columns_to_rows(in_list[0:ind])))
        in_list = in_list[ind+1:]
    reflection_line_row.append(_find_reflection_line(in_list))
    reflection_line_col.append(_find_reflection_line(_columns_to_rows(in_list)))
    return sum(reflection_line_col) + 100*sum(reflection_line_row)


def _find_reflection_line(in_pattern):
    reflection_line = 0
    for row_num, row in enumerate(in_pattern):
        if row_num+1 < len(in_pattern):
            if _check_if_reflected([row], [in_pattern[row_num+1]]):
                if _propagate_reflections(row_num, row_num+1, in_pattern):
                    reflection_line = row_num+1
                    break
            else:
                continue
    return reflection_line

def _propagate_reflections(row_num_left, row_num_right, in_pattern):
    if row_num_left-1>=0 and row_num_right+1 < len(in_pattern):
        if _check_if_reflected(in_pattern[row_num_left-1], in_pattern[row_num_right+1]):
            return _propagate_reflections(row_num_left-1, row_num_right+1, in_pattern)
        else:
            return False
    return True

def _check_if_reflected(in_first, in_second):
    if collections.Counter(in_first) == collections.Counter(in_second):
        return True
    else:
        return False
    
def _columns_to_rows(in_list):
    in_list = [[*_] for _ in in_list]
    new_list = list(map(list, zip(*in_list)))
    new_list = [''.join(_) for _ in new_list]
    return new_list

def solve_part_two(in_list):
    '''
    Solves part two.
    '''
    return False

with open('input.txt', 'r', encoding="utf-8") as file:
    NUMBERS = file.readlines()

NUMBERS = [x.strip() for x in NUMBERS]

print(solve_part_one(NUMBERS))
print(solve_part_two(NUMBERS))