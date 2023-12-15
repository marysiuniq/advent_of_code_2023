# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 05:59:56 2023

@author: Marysia
"""

def solve_part_one(in_list):
    '''
    Solves part one.
    '''
    result = 0
    for _ in in_list[0].split(','):
        result += _hash_algorithm(_)
    return result

def _hash_algorithm(in_list):
    current_value = 0
    for _ in in_list:
        current_value += ord(_)
        current_value *= 17
        current_value = current_value % 256
    return current_value

def _check_if_lens_in_box(label, box):
    for ind, _ in enumerate(box):
        if _[0] == label:
            return ind
        else:
            continue
    return -1

def _focusing_power(boxes):
    focusing_power = 0
    for key, value in boxes.items():
        for slot, lense in enumerate(value):
            focusing_power += (1 + key)*(slot+1)*lense[1]
    return focusing_power
        
def solve_part_two(in_list):
    '''
    Solves part two.
    '''
    boxes = {_:[] for _ in range(256)}
    for _ in in_list[0].split(','):
        if '=' in _:
            sequence = _.split('=')
            label = sequence[0]
            focal_len = int(sequence[1])
            box_id = _hash_algorithm(label)
            box_inside = boxes[box_id]
            index = _check_if_lens_in_box(label, box_inside)
            if index >=0:
                if index < len(box_inside)-1:
                    boxes[box_id] = box_inside[0:index] + [[label, focal_len]] + box_inside[index+1:]
                elif index:
                    boxes[box_id] = box_inside[0:index] + [[label, focal_len]]
                elif index == 0:
                    boxes[box_id] = [[label, focal_len]] + box_inside[index+1:]
            else:
                boxes[box_id].append([label, focal_len])
        elif '-' in _:
            label = _[0:-1]
            box_id = _hash_algorithm(label)
            box_inside = boxes[box_id]
            index = _check_if_lens_in_box(label, box_inside)
            if index >= 0:
                boxes[box_id].remove(boxes[box_id][index])
        else:
            print('Wrong sequence.')    
    return _focusing_power(boxes)
    

with open('input.txt', 'r', encoding="utf-8") as file:
    NUMBERS = file.readlines()

NUMBERS = [x.strip() for x in NUMBERS]

print(solve_part_one(NUMBERS))
print(solve_part_two(NUMBERS))
