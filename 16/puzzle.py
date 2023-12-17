# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 08:31:46 2023

@author: Marysia & Piotr
"""

def solve_part_one(in_list):
    '''
    Solves part one.
    '''
    in_list = [list(_) for _ in in_list]
    visited = _propagate_beam(in_list, (0,0), (0,1))
    return len(visited)

def _propagate_beam(in_list, start_pos, start_dir):
    stack = [(start_pos,start_dir)] # position, direction
    visited_states = set()
    lim_hor = len(in_list[0])
    lim_ver = len(in_list)
    while stack:
        cur_pos, cur_dir = stack.pop()
        if cur_pos[0] < 0 or cur_pos[0] >= lim_ver:
            continue
        if cur_pos[1] < 0 or cur_pos[1] >= lim_hor:
            continue
        if (cur_pos, cur_dir) in visited_states:
            continue
        visited_states.add((cur_pos, cur_dir))
        cur_symb = in_list[cur_pos[0]][cur_pos[1]]
        if cur_symb == '\\':
            tmp_dir = (cur_dir[1], cur_dir[0])
            tmp_pos = _move_beam(cur_pos, tmp_dir)
            stack.append((tmp_pos, tmp_dir))
        elif cur_symb == '/':
            tmp_dir = (-cur_dir[1], -cur_dir[0])
            tmp_pos = _move_beam(cur_pos, tmp_dir)
            stack.append((tmp_pos, tmp_dir))
        elif cur_symb == '|':
            if cur_dir in ((0,1),(0,-1)):
                tmp_dir = (1,0)
                tmp_pos = _move_beam(cur_pos, tmp_dir)
                stack.append((tmp_pos, tmp_dir))
                tmp_dir = (-1,0)
                tmp_pos = _move_beam(cur_pos, tmp_dir)
                stack.append((tmp_pos, tmp_dir))
            else:
                tmp_pos = _move_beam(cur_pos, cur_dir)
                stack.append((tmp_pos, cur_dir))
        elif cur_symb == '-':
            if cur_dir in ((-1,0),(1,0)):
                tmp_dir = (0,1)
                tmp_pos = _move_beam(cur_pos, tmp_dir)
                stack.append((tmp_pos, tmp_dir))
                tmp_dir = (0,-1)
                tmp_pos = _move_beam(cur_pos, tmp_dir)
                stack.append((tmp_pos, tmp_dir))
            else:
                tmp_pos = _move_beam(cur_pos, cur_dir)
                stack.append((tmp_pos, cur_dir))
        else:
            assert cur_symb == '.'
            tmp_pos = _move_beam(cur_pos, cur_dir)
            stack.append((tmp_pos, cur_dir))
    return {_[0] for _ in visited_states}

def _move_beam(in_pos, in_dir):
    return (in_pos[0]+in_dir[0], in_pos[1]+in_dir[1])

def solve_part_two(in_list):
    '''
    Solves part two.
    '''
    in_list = [list(_) for _ in in_list]
    best = 0
    for pos in range(len(in_list[0])):
        visited = _propagate_beam(in_list, (0,pos), (1,0))
        best = max(best, len(visited))
        visited = _propagate_beam(in_list, (len(in_list)-1,pos), (-1,0))
        best = max(best, len(visited))
    for pos in range(len(in_list)):
        visited = _propagate_beam(in_list, (pos,0), (0,1))
        best = max(best, len(visited))
        visited = _propagate_beam(in_list, (pos,len(in_list[0])-1), (0,-1))
        best = max(best, len(visited))
    return best

with open('input.txt', 'r', encoding="utf-8") as file:
    INPUT = file.readlines()

INPUT = [x.strip() for x in INPUT]

print(solve_part_one(INPUT))
print(solve_part_two(INPUT))
