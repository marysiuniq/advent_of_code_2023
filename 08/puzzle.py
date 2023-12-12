#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 09:57:22 2023

@author: mariapasz
"""
from math import gcd
def solve_part_one(in_list):
    '''
    Solves part one.
    '''
    directions, positions_dict = _prepare_directions(in_list)
    steps_count = 0
    position = 'AAA'
    while position != 'ZZZ':
        for _ in directions:
            steps_count += 1
            if _ == 'L':
                position = positions_dict[position][0]
            else:
                position = positions_dict[position][1]
            if position == 'ZZZ':
                break
    return steps_count

def _prepare_directions(in_list):
    directions = in_list[0]
    positions_dict = {}
    for row in in_list[2:]:
        positions_dict[row[0:3]] = [row[7:10], row[12:15]]
    return directions, positions_dict

def _check(in_list, char):
    return all(i == char for i in in_list)


def lcm(in_num):
    '''
    Calculates lowest common multiplier.
    '''
    result = 1
    for i in in_num:
        result = result*i//gcd(result, i)
    return result

def solve_part_two(in_list):
    '''
    Solves part two.
    '''
    directions, positions_dict = _prepare_directions(in_list)
    positions = []
    for pos in positions_dict:
        if pos[2] == 'A':
            positions.append(pos)
    positions_z = []
    steps_z = []
    for pos in positions:
        steps_count = 0
        position = pos
        while not position[2] == 'Z':
            for _ in directions:
                steps_count += 1
                if _ == 'L':
                    position = positions_dict[position][0]
                else:
                    position = positions_dict[position][1]
                if position[2] == 'Z':
                    positions_z.append([position, steps_count])
                    steps_z.append(steps_count)
                    break
    return lcm(steps_z)

with open('input.txt', 'r', encoding="utf-8") as file:
    NUMBERS = file.readlines()

NUMBERS = [x.strip() for x in NUMBERS]

print(solve_part_one(NUMBERS))
print(solve_part_two(NUMBERS))
