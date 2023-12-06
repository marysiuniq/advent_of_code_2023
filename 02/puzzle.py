# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 05:55:00 2023

@author: Marysia

Puzzle 2 from https://adventofcode.com/2023/day/2
"""

def solve_part_one(in_list):
    '''
    Solves part one: calculates the sum of the IDs of those games.
    '''
    result = 0
    reds = 0
    greens = 0
    blues = 0
    for _, row in enumerate(in_list):
        new_row = row.split()
        game_num = int(new_row[1][0:-1])
        reds = 0
        greens = 0
        blues = 0
        pos = 3
        check_set = 0
        sets_num = row.count(';') + 1
        for _, item in enumerate(new_row[3::2]):
            if not ';' in item:
                print(item)
                reds += ('red' in item)*int(new_row[pos-1])
                greens += ('green' in item)*int(new_row[pos-1])
                blues += ('blue' in item)*int(new_row[pos-1])
            else:
                reds += ('red' in item)*int(new_row[pos-1])
                greens += ('green' in item)*int(new_row[pos-1])
                blues += ('blue' in item)*int(new_row[pos-1])
                if reds <= 12 and greens <= 13 and blues <= 14:
                    check_set += 1
                else:
                    check_set = 0
                    break
                reds = 0
                greens = 0
                blues = 0
            pos = pos + 2
        if reds <=12 and greens <= 13 and blues <= 14:
            check_set += 1
        else:
            check_set = 0
        if check_set == sets_num:
            print('game number' + str(game_num))
            result += game_num
    return result

def solve_part_two(in_list):
    '''
    Solves part two: computes the sum of the power of the sets.
    '''
    result = 0
    for _, row in enumerate(in_list):
        max_reds = 0
        max_greens = 0
        max_blues = 0
        set_power = 1
        new_row = row.split()#
        game_num = int(new_row[1][0:-1])
        pos = 3
        for _, item in enumerate(new_row[3::2]):
            print(item)
            if ('red' in item)*int(new_row[pos-1]) > max_reds:
                max_reds = int(new_row[pos-1])
            if ('green' in item)*int(new_row[pos-1]) > max_greens:
                max_greens = int(new_row[pos-1])
            if ('blue' in item)*int(new_row[pos-1]) > max_blues:
                max_blues = int(new_row[pos-1])
            pos = pos + 2
        print('game number ' + str(game_num))
        set_power = max_reds*max_greens*max_blues
        print('set power ' + str(set_power))
        result += set_power
    return result

with open('input.txt', 'r') as file:
    NUMBERS = file.readlines()

NUMBERS = [x.strip() for x in NUMBERS]

print(solve_part_one(NUMBERS))
print(solve_part_two(NUMBERS))
