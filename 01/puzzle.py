# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 05:52:23 2023

@author: Marysia

Puzzle 1 from https://adventofcode.com/2023/day/1
"""

import numpy as np

def solve_part_one(in_list):
    '''
    Solves part one.
    '''
    return sum(_extract_num(row) for row in in_list)

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

print(solve_part_one(NUMBERS))
print(solve_part_two(NUMBERS))
