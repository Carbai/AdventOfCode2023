import re
import itertools
import math

with open("input.txt") as ifile:
    input = ifile.read().splitlines()

def find_symbols(lines:list) -> list:
    sym_ind_lst=[]
    n = 0
    for line in lines:
        matches = re.finditer(r'[^.\d]', line)
        match = [m.start() for m in matches]
        for m in match:
            sym_ind_lst.append([n, m])
        n += 1
    return sym_ind_lst

def find_symbols_part_two(lines:list) -> list:
    sym_ind_lst=[]
    n = 0
    for line in lines:
        matches = re.finditer(r'[\\*]', line)
        match = [m.start() for m in matches]
        for m in match:
            sym_ind_lst.append([n, m])
        n += 1
    return sym_ind_lst

def get_surroundings(indeces_list: list, n: int, m: int) -> list:
    surr_ind = []
    for indeces in indeces_list:
        tmp_lst=[]
        row = indeces[0]
        col = indeces[1]
        
        if row==0:
            if col == 0:
                ind = [[row, col+1],[row+1, col],[row+1, col+1]]
            elif col ==m-1:
                ind = [[row, col-1],[row+1, col-1],[row+1, col]]
            else:
                ind = [[row, col-1],[row, col+1],[row+1, col-1],[row+1, col],[row+1, col+1]]
        elif row==n-1:
            if col == m-1:
                ind = [[row-1, col-1], [row-1, col], [row, col-1]]
            elif col==0:
                ind = [[row-1, col], [row-1, col+1], [row, col+1]]
            else:
                ind = [[row-1, col-1], [row-1, col], [row-1, col+1], [row, col-1],[row, col+1]]
        elif col==0:
                ind = [[row-1, col], [row-1, col+1], [row, col+1],[row+1, col],[row+1, col+1]]
        elif col==m-1:
                ind = [[row-1, col-1], [row-1, col], [row, col-1],[row+1, col-1],[row+1, col]]
        else:
            ind = [[row-1, col-1], [row-1, col], [row-1, col+1], [row, col-1],[row, col+1],[row+1, col-1],[row+1, col],[row+1, col+1]]
        surr_ind.extend(ind)
    surr_ind.sort()
    return list(k for k,_ in itertools.groupby(surr_ind))

def find_digit(lines:list, indeces:list) -> list:
    for idx in indeces[::-1]:
        if not lines[idx[0]][idx[1]].isdigit():
            indeces.remove(idx)
    return indeces

def find_digit_part_two(lines:list, indeces:list) -> list:
    for idx in indeces[::-1]:
        if not lines[idx[0]][idx[1]].isdigit():
            indeces.remove(idx)
    
    for idx in indeces[::-1]:
        dist_lst = [math.dist(idx, y) for y in indeces]
        if 1 in dist_lst:
            indeces.remove(idx)
    return indeces

def get_right_gears(neighbours: list, asterisks: list) -> list:
    
    for asterisk in asterisks[::-1]:
        count=0  
        dist=[math.dist(asterisk, neighbour) for neighbour in neighbours]
        if 1 in dist:  
            tmp=dist.count(1)
            count+=tmp
        if math.dist([0,0],[1,1]) in dist:
            tmp=dist.count(math.dist([0,0],[1,1]))
            count+=tmp
        if count != 2:
            asterisks.remove(asterisk)
    return asterisks

def get_numbers(lines: list, indeces: list) -> list:
    dgts = []
    for idx in indeces:
        digit = []
        back_idx = idx[1]
        forth_idx = idx[1]
        back = lines[idx[0]][0:idx[1]+1]
        forth = lines[idx[0]][idx[1]+1::]
        
        for val in back[::-1]:
            back_idx-=1
            if val.isdigit():
                digit.extend(val)
                tmp_lst = list(lines[idx[0]])
                tmp_lst[back_idx]='.'
                lines[idx[0]]=''.join(tmp_lst)
            else:
                break
        digit.reverse()
        
        for val in forth:
            forth_idx += 1
            if val.isdigit():
                digit.extend(val)
                tmp_lst = list(lines[idx[0]])
                tmp_lst[forth_idx]='.'
                lines[idx[0]]=''.join(tmp_lst)
            else:
                break  
        dgts.append(''.join(digit))
    int_lst = list(itertools.filterfalse(lambda x: x == '', dgts))
    int_lst = [int(x) for x in int_lst]
    return int_lst

def get_numbers_part_two(asterisks: list, neighbours: list, lines: list) -> list:
    gear_ratio_lst=[]
    for asterisk in asterisks:
        gear_ratio=[]
        for neighbour in neighbours:
            if math.dist(asterisk, neighbour) == 1 or math.dist(asterisk, neighbour) == math.dist([0,0],[1,1]):
                digit = []
                back_idx = neighbour[1]
                forth_idx = neighbour[1]
                back = lines[neighbour[0]][0:neighbour[1]+1]
                forth = lines[neighbour[0]][neighbour[1]+1::]
        
                for val in back[::-1]:
                    back_idx-=1
                    if val.isdigit():
                        digit.extend(val)
                    else:
                        break
                digit.reverse()
        
                for val in forth:
                    forth_idx += 1
                    if val.isdigit():
                        digit.extend(val)
                    else:
                        break  
                
                gear_ratio.append(''.join(digit))
                gear_ratio = list(itertools.filterfalse(lambda x: x == '', gear_ratio))
                
        gear_ratio_lst.append(int(gear_ratio[0])*int(gear_ratio[1]))
    return gear_ratio_lst
 
#indeces_lst=find_symbols(input)
asterisk_lst=find_symbols_part_two(input)
#indeces_to_chk=get_surroundings_part_one(indeces_lst, len(input), len(input[0]))
indeces_to_chk_part_two=get_surroundings(asterisk_lst, len(input), len(input[0]))

digit_indices_part_two = find_digit_part_two(input, indeces_to_chk_part_two)
gears_lst=get_right_gears(indeces_to_chk_part_two, asterisk_lst)
gears_surroundings=get_surroundings(gears_lst, len(input), len(input[0]))
gears_digits=find_digit_part_two(input, gears_surroundings)
gears_digits_lst=get_numbers_part_two(gears_lst,gears_digits,input)
#result_list = [gears_digits_lst[i] * gears_digits_lst[i + 1] for i in range(0, len(gears_digits_lst), 2)]
print(type(gears_digits_lst[1]))
print('Part two: ', sum(gears_digits_lst))
#digit_indices=find_digit(input, indeces_to_chk)

#digits_lst = get_numbers(input, digit_indices)

#print('Part one: ', sum(digits_lst))
