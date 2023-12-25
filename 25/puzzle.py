# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 06:01:18 2023

@author: Marysia & Piotr

Puzzle 25 from https://adventofcode.com/2023/day/25
"""

import math
import networkx as nx


def _solve_part_one(in_list):
    graph = _prepare_data(in_list)
    edges_to_remove = nx.minimum_edge_cut(graph)
    graph.remove_edges_from(edges_to_remove)
    components = nx.connected_components(graph)
    return math.prod(len(_) for _ in components)

def _prepare_data(in_list):
    graph = nx.Graph()
    for line in in_list:
        node, others = line.split(': ')
        for other_node in others.split():
            graph.add_edge(node, other_node)
    return graph

with open("input.txt", "r", encoding="utf-8") as file:
    INPUT = file.readlines()

INPUT = [x.strip() for x in INPUT]

print(_solve_part_one(INPUT))
