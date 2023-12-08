from audioop import reverse
from nis import match
import re
from typing import final

def parse_input(file):
    my_dict={}
    with open(file) as ifile:
        input=ifile.read().splitlines()
   # hands=[]
   # bids=[]

    for data in input:
    #    hands.append(data.split()[0]) 
     #   bids.append(data.split()[-1])
        my_dict[data.split()[0]]=int(data.split()[-1])
    return my_dict

def get_hand_type(hands: list):
    my_dict={'five':[],
            'four': [],
            'full': [],
            'three': [],
            'two': [],
            'one':[],
            'high': []
    }
    for hand in hands:
        matches={}
        for i in hand:
            if i in matches:
                matches[i] += 1
            else:
                matches[i] = 1
        values=list(matches.values())
        if 5 in values:
            my_dict['five'].append(hand)
        elif 4 in values:
            my_dict['four'].append(hand)
        elif 3 in values and 2 in values:
            my_dict['full'].append(hand)
        elif 3 in values:
            my_dict['three'].append(hand)
        elif values.count(2)==2:
            my_dict['two'].append(hand)
        elif 2 in values:
            my_dict['one'].append(hand)
        else:
            my_dict['high'].append(hand)
    return my_dict


def get_hand_type_part2(hands: list):
    my_dict={'five':[],
            'four': [],
            'full': [],
            'three': [],
            'two': [],
            'one':[],
            'high': []
    }
    for hand in hands:
        matches={}
        for i in hand:
            if i == 'J':
                continue
            if i in matches:
                matches[i] += 1
            else:
                matches[i] = 1
        values=list(matches.values())
        if 5 in values or hand.count('J') == 5 or (4 in values and hand.count('J')==1) or (3 in values and hand.count('J')==2) or (2 in values and hand.count('J')==3) or hand.count('J')==4:
            my_dict['five'].append(hand)
        elif 4 in values or (3 in values and hand.count('J')==1) or (2 in values and hand.count('J')==2) or (1 in values and hand.count('J')==3):
            print(values)
            my_dict['four'].append(hand)
        elif (3 in values and 2 in values) or (values.count(2)==2 and hand.count('J')==1):
            my_dict['full'].append(hand)
        elif 3 in values or (2 in values and hand.count('J')==1) or (1 in values and hand.count('J')==2):
            my_dict['three'].append(hand)
        elif values.count(2)==2:
            my_dict['two'].append(hand)
        elif 2 in values or (1 in values and hand.count('J')==1):
            my_dict['one'].append(hand)
        else:
            my_dict['high'].append(hand)
    return my_dict

def custom_sort(input_list):
    def custom_key(s):
        #part one
       # order = {'A': 0, 'K': 1, 'Q': 2, 'J': 3, 'T': 4, '9': 5, 
        #        '8': 6, '7': 7, '6': 8,
         #       '5': 9, '4': 10, '3': 11, '2': 12}
        #part two
        order = {'A': 0, 'K': 1, 'Q': 2, 'T': 3, '9': 4, 
                '8': 5, '7': 6, '6': 7,
                '5': 8, '4': 9, '3': 10, '2': 11, 'J': 12}
     #   print([order.get(char, float('inf')) for char in s],s)
        return [order.get(char, float('inf')) for char in s]
    
    sorted_list = sorted(input_list, key=custom_key)
    return sorted_list


dict_input=parse_input('input.txt')

#part one
#dict_hands=get_hand_type(hands)
#part two
dict_hands=get_hand_type_part2(dict_input.keys())
print(dict_hands)
for key, value in dict_hands.items():
    dict_hands[key]=custom_sort(value)


flattened_list = [item for sublist in dict_hands.values() for item in sublist]
reversed_lst = flattened_list[::-1]
score=[]
#print(reversed_lst,len(reversed_lst))
for n,val in enumerate(reversed_lst):
 #   print(n,val,dict_input[val])
    score.append((n+1)*dict_input[val])

print('Part one:', sum(score))
