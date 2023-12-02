import re

with open('input.txt') as ifile:
    lines = ifile.readlines()

cubes_dict = {'red': 12,
              'green': 13,
              'blue': 14
}

def is_game_possible(cubes_sets: list) -> bool:
    games_poss_list = []
    for cubes_set in cubes_sets:
        cubes_per_colors = cubes_set.split(',')
        for cubes_per_color in cubes_per_colors:
            games_poss_list.append(int(cubes_per_color.strip().split(' ')[0]) <= cubes_dict[cubes_per_color.split()[-1]])
    return games_poss_list
        

def part_one(lines: list) -> int:
    game_id = 0
    game_id_list = []
    for line in lines:
        cubes_revealed_lst=line.split(':')[-1].split(';')
        game_id += 1
        if False not in is_game_possible(cubes_revealed_lst):
            game_id_list.append(game_id)
    return sum(game_id_list)

def part_two(lines: list) -> int:
    power_set_list=[]
    for line in lines:
        matches_red = max([int(x) for x in re.findall(r'\d+(?:/\d+)?(?=\s?red?\b)', line)])
        matches_blue = max([int(x) for x in re.findall(r'\d+(?:/\d+)?(?=\s?blue?\b)', line)])
        matches_green = max([int(x) for x in re.findall(r'\d+(?:/\d+)?(?=\s?green?\b)', line)])
        power_set_list.append(matches_red*matches_blue*matches_green)
    return sum(power_set_list)

print('Part One: ', part_one(lines))
print('Part Two: ', part_two(lines))
