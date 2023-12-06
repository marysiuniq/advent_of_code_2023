# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 05:59:34 2023

@author: Marysia
"""

import numpy as np

def solve_part_one(in_list):
    '''
    Solves part one.
    '''
    times = in_list[0].split()[1:]
    distances= in_list[1].split()[1:]
    ways_win = []
    for time, distance in zip(times, distances):
        ways_win.append(_calc_number_of_wins(time, distance))
    return np.prod(ways_win)

def _calc_number_of_wins(time, distance):
    num_wins = 0
    for hold_time in range(int(time)):
        new_distance = (int(time)-hold_time)*hold_time
        if new_distance > int(distance):
            num_wins += 1
        elif num_wins > 0:
            break
    return num_wins
    
def solve_part_two(in_list):
    '''
    Solves part two.
    '''
    time = int(''.join(in_list[0]).replace(' ', '')[5:])
    distance = int(''.join(in_list[1]).replace(' ', '')[9:])
    return _calc_number_of_wins(time, distance)

with open('input.txt', 'r', encoding="utf-8") as file:
    NUMBERS = file.readlines()

NUMBERS = [x.strip() for x in NUMBERS]

print(solve_part_one(NUMBERS))
print(solve_part_two(NUMBERS))