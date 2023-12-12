#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 06:15:41 2023

@author: mariapasz
"""
from itertools import combinations
import math

def solve_part_one(in_list):
    '''
    Solves part one.
    '''
    for row in in_list:
        row = in_list[1]
        separator = row.index(' ')
        row_len = len(row[0:separator])
        n_groups = len(row[separator+1:].split(','))
        numbers = [int(_) for _ in row[separator+1:].split(',')]
        len_marked = sum(numbers)
        n_empty = row_len - len_marked - n_groups + 1
        opts = combinations(range(n_groups+n_empty), n_groups)
    return opts

# def _count_combinations(in_row):
#     separator = row.index(' ')
#     row_len = len(row[0:separator])
#     n_groups = len(row[separator+1:].split(','))
#     numbers = [int(_) for _ in row[separator+1:].split(',')]
#     len_marked = sum(numbers)
#     n_empty = row_len - len_marked - n_groups + 1
#     return math.factorial(n_groups + n_empty)/math.factorial(n_groups)
    

def _create_possibilities(self, n_empty, groups, ones):
    # from https://gist.github.com/henniedeharder/d7af7462be3eed96e4a997498d6f9722#file-nonogramsolver-py
    # Nanograms: https://towardsdatascience.com/solving-nonograms-with-120-lines-of-code-a7c6e0f627e4
        res_opts = []
        for p in combinations(range(groups+n_empty), groups):
            selected = [-1]*(groups+n_empty)
            ones_idx = 0
            for val in p:
                selected[val] = ones_idx
                ones_idx += 1
            res_opt = [ones[val]+[-1] if val > -1 else [-1] for val in selected]
            res_opt = [item for sublist in res_opt for item in sublist][:-1]
            res_opts.append(res_opt)
        return res_opts

def solve_part_two(in_list):
    '''
    Solves part two.
    '''

    return 0

with open('test.txt', 'r', encoding="utf-8") as file:
    NUMBERS = file.readlines()

NUMBERS = [x.strip() for x in NUMBERS]

test = solve_part_one(NUMBERS)
print(solve_part_one(NUMBERS))
#print(solve_part_two(NUMBERS))
