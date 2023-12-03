# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 05:55:19 2023

@author: Marysia
"""

import numpy as np
import re
import itertools

def solve_part_one(in_list):
    '''
    Solves part one.
    '''
    numbers = []
    result = 0
    for row, item in enumerate(in_list):
        numbers_tmp = re.findall(r'\d+', item)
        pos_start = [m.start() for m in re.finditer(r'\d+', item)]
        pos_end = [p + len(n) for p, n in zip(pos_start, numbers_tmp)]
        rows = [row-1,row,row+1]
        for s, e, num in zip(pos_start, pos_end, numbers_tmp):
            cols = list(range(s-1, e+1))
            is_break = 0
            for r in rows:
                if r>=0 and r < len(item):
                    for c in cols:
                        if c >=0 and c < len(in_list) and (not in_list[r][c].isdigit()) and (not in_list[r][c]=='.'):
                            numbers.append(num)
                            result += int(num)
                            is_break = 1
                            break
                if is_break==1:
                    break
        # for num in numbers_tmp:
        #     pos_start = item.find(num)
        #     pos_end = pos_start + len(num)
        #     rows = [row-1,row,row+1]
        #     cols = list(range(pos_start-1, pos_end+1))
        #     is_break = 0
        #     for r in rows:
        #         if r>=0 and r < len(item):
        #             for c in cols:
        #                 if c >=0 and c < len(in_list) and (not in_list[r][c].isdigit()) and (not in_list[r][c]=='.'):
        #                     numbers.append(num)
        #                     result += int(num)
        #                     is_break = 1
        #                     break
        #         if is_break==1:
        #             break
   # res= set(numbers)
   # sum(int(_) for _ in res)
    return result

def _find_first_digit(in_str):
    return next(_ for _ in in_str if _.isdigit())

def _extract_num(in_row):
    first_digit = _find_first_digit(in_row)
    last_digit = _find_first_digit(in_row[::-1])
    return int(first_digit + last_digit)
    

def solve_part_two(in_list):
    '''
    Solves part two.
    '''
    numbers_dict = {'one': '1', 'two': '2', 'three': '3', 'four': '4',
                    'five': '5', 'six': '6', 'seven': '7', 'eight': '8',
                    'nine': '9'}
    digits = []
    for _, row in enumerate(in_list):
        row_new = row
        for _, number in enumerate(numbers_dict.keys()):
            row_new = row_new.replace(number,number[0]+numbers_dict[number]+number[-1])
        for _, digit in enumerate(row_new):
            if digit.isdigit():
                digits.append(int(digit))
                break
        for _, digit in enumerate(row_new[::-1]):
            if digit.isdigit():
                digits.append(int(digit))
                break
    return 10*np.sum(digits[::2]) + np.sum(digits[1::2])

with open('input.txt', 'r', encoding="utf-8") as file:
    NUMBERS = file.readlines()

NUMBERS = [x.strip() for x in NUMBERS]


test = solve_part_one(NUMBERS)

#assert test == 525911
print(solve_part_one(NUMBERS))
#print(solve_part_two(NUMBERS))
