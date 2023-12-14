#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 06:00:57 2023

@author: mariapasz
"""
import matplotlib.pyplot as plt

def solve_part_one(in_list):
    '''
    Solves part one.
    '''
    list_tilted = _tilt_the_platform(in_list)
    return _calculate_load(list_tilted)
    
def _calculate_load(in_list):
    ind = len(in_list)
    total_load = 0
    ind = 0
    for amount in range(len(in_list),0,-1):
        total_load += amount*in_list[ind].count('O')
        ind += 1
    return total_load

def _tilt_the_platform(in_list):
    for row_ind in range(1,len(in_list)):
        row = in_list[row_ind]
        for pos in range(len(row)):
            if in_list[row_ind][pos] == 'O':
                ind = row_ind
                while ind-1 >=0:
                    if in_list[ind-1][pos] == '.':
                        if pos < len(row)-1:
                            in_list[ind] = in_list[ind][0:pos] + '.' + in_list[ind][pos+1:]
                        else:
                            in_list[ind] = in_list[ind][0:pos] + '.'
                        #in_list[ind][pos] = '.'
                        if pos < len(row)-1:
                            in_list[ind-1] = in_list[ind-1][0:pos] + 'O' + in_list[ind-1][pos+1:]
                        else:
                            in_list[ind-1] = in_list[ind-1][0:pos] + 'O'
                        #in_list[ind-1][pos] = '0'
                        ind -= 1
                    else:
                        break
            else:
                continue
    return in_list

def _one_cycle(in_list):
    in_list = _tilt_the_platform(in_list) # north
    in_list = _tilt_the_platform(_columns_to_rows(in_list)) # east
    in_list = _columns_to_rows(in_list) # east
    in_list = _tilt_the_platform(in_list[::-1]) #south
    in_list = in_list[::-1] #south
    in_list = _tilt_the_platform(_columns_to_rows(in_list)[::-1]) # west
    in_list = _columns_to_rows(in_list) # west
    in_list = [_[::-1] for _ in in_list] # west
    return in_list

def _columns_to_rows(in_list):
    in_list = [[*_] for _ in in_list]
    new_list = list(map(list, zip(*in_list)))
    new_list = [''.join(_) for _ in new_list]
    return new_list


def solve_part_two(in_list):
    '''
    Solves part two.
    '''
    total_load = []
    for _ in range(200):
        in_list = _one_cycle(in_list)
        total_load.append(_calculate_load(in_list))
    # works only for my input so far
    # TO-DO: find the period automatically
    return (10**9 - 199)%9 + total_load[198]
    

with open('input.txt', 'r', encoding="utf-8") as file:
    NUMBERS = file.readlines()

NUMBERS = [x.strip() for x in NUMBERS]

print(solve_part_one(NUMBERS))
print(solve_part_two(NUMBERS))
