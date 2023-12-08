import copy
from copy import deepcopy
import math

def parse_input(filename: str) -> dict:
    with open(filename) as ifile:
        lines=ifile.read().splitlines()
        instructions=list(lines[0].strip(""))
        my_dict={}
        for line in lines:
            if '=' in line:
                my_dict[line.split('=')[0].strip()] = line.split('=')[-1].strip().replace('(','').replace(')','').split(',')
        return instructions, my_dict

def get_new_node(direction: str) -> int:
    if direction=='L':
        return 0
    else:
        return 1

def navigate_network(direction: list, map: dict) -> int:
    end='ZZZ'
    start='AAA'
    curr_node=start
    moves=0
    backup_directions=direction[:]
    while curr_node != end:
        
        if not direction:
            direction.extend(backup_directions)
    #    print(curr_node, moves)
        curr_node=map[curr_node][get_new_node(direction[0])].strip()
        moves+=1
     #   print(curr_node, moves)
        direction.pop(0)
    return moves

def navigate_network_part2(direction: list, map: dict) -> int:
    end=[x for x in map.keys() if x[-1]=='Z']
    start=[x for x in map.keys() if x[-1]=='A']
   # curr_nodes=start[:]
    moves=[]
    backup_directions=direction[:]
    for node in start:
        move=0
        while node not in end:
          #  print(node)
            if not direction:
                direction.extend(backup_directions)
            node=map[node][get_new_node(direction[0])].strip()
            move+=1
    #    print(curr_nodes, moves)
            direction.pop(0)
        moves.append(move)
    return math.lcm(*moves)
instructions, map_dict=parse_input('input.txt')
#print(instructions, map_dict)
#print('Part One:', navigate_network(instructions,map_dict)) 
print('Part One:', navigate_network_part2(instructions,map_dict)) 
