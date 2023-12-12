#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 05:57:22 2023

@author: mariapasz
"""
def solve_part_one(in_list):
    '''
    Solves part one.
    '''
    seeds_list = in_list[0].split()[1:]
    to_soil_ind = in_list.index('seed-to-soil map:')+1
    to_fert_ind = in_list.index('soil-to-fertilizer map:')+1
    to_water_ind = in_list.index('fertilizer-to-water map:')+1
    to_light_ind = in_list.index('water-to-light map:')+1
    to_temp_map_ind = in_list.index('light-to-temperature map:')+1
    to_humid_ind = in_list.index('temperature-to-humidity map:')+1
    to_loc_ind = in_list.index('humidity-to-location map:')+1
    location_min = 32290612640000000
    #locations = []
    print(seeds_list)
    for seed in seeds_list:
        print('for seed '+seed)
        soil = _search_in_map(seed, in_list[to_soil_ind:to_fert_ind-2])
        fertilizer = _search_in_map(soil, in_list[to_fert_ind:to_water_ind-2])
        water = _search_in_map(fertilizer, in_list[to_water_ind:to_light_ind-2])
        light = _search_in_map(water, in_list[to_light_ind:to_temp_map_ind-2])
        temperature = _search_in_map(light, in_list[to_temp_map_ind:to_humid_ind-2])
        humidity = _search_in_map(temperature, in_list[to_humid_ind:to_loc_ind-2])
        location = _search_in_map(humidity, in_list[to_loc_ind:])
        #locations = locations.append(location) # doesn't work, no idea why
        print(location)
        if location < location_min:
            location_min = location
    return location_min

def _search_in_map(seed, in_list):
    #print(seed)
    for row in in_list:
        row = row.split()
        #print(row)
        source_start = int(row[1])
        range_val = int(row[2])
        if int(seed) >= source_start and int(seed) < source_start + range_val:
            soil = int(seed) - source_start + int(row[0])
            break
        else:
            soil = int(seed)
    #print(soil)
    return soil

def _create_seeds_list(in_list):
    seeds_list = []
    iterator = 1
    for num in in_list[::2]:
        seeds_list += list(range(int(num),int(num)+int(in_list[iterator])))
        iterator += 2
    return [str(_) for _ in seeds_list]


def solve_part_two(in_list):
    '''
    Solves part two.
    '''
    seeds_list = _create_seeds_list(in_list[0].split()[1:])
    to_soil_ind = in_list.index('seed-to-soil map:')+1
    to_fert_ind = in_list.index('soil-to-fertilizer map:')+1
    to_water_ind = in_list.index('fertilizer-to-water map:')+1
    to_light_ind = in_list.index('water-to-light map:')+1
    to_temp_map_ind = in_list.index('light-to-temperature map:')+1
    to_humid_ind = in_list.index('temperature-to-humidity map:')+1
    to_loc_ind = in_list.index('humidity-to-location map:')+1
    location_min = 32290612640000000
    #locations = []
    #print(seeds_list)
    # for seed in seeds_list:
    #     #print('for seed '+seed)
    #     soil = _search_in_map(seed, in_list[to_soil_ind:to_fert_ind-2])
    #     fertilizer = _search_in_map(soil, in_list[to_fert_ind:to_water_ind-2])
    #     water = _search_in_map(fertilizer, in_list[to_water_ind:to_light_ind-2])
    #     light = _search_in_map(water, in_list[to_light_ind:to_temp_map_ind-2])
    #     temperature = _search_in_map(light, in_list[to_temp_map_ind:to_humid_ind-2])
    #     humidity = _search_in_map(temperature, in_list[to_humid_ind:to_loc_ind-2])
    #     location = _search_in_map(humidity, in_list[to_loc_ind:])
    #     #locations = locations.append(location) # doesn't work, no idea why
    #     #print(location)
    #     if location < location_min:
    #         location_min = location
    #return location_min
    return seeds_list

with open('input.txt', 'r', encoding="utf-8") as file:
    NUMBERS = file.readlines()

NUMBERS = [x.strip() for x in NUMBERS]

#print(solve_part_one(NUMBERS))
print(solve_part_two(NUMBERS))#