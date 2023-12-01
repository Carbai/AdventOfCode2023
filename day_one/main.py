import re
with open('input_part1.txt') as ifile:
    lines = ifile.readlines()

def part_1(file_lines:list) -> int:
    codes = []

    for line in file_lines:
        line_code = re.findall(r'\d', line)
        codes.append(int(line_code[0]+line_code[-1]))
    return sum(codes)

def convert_words_to_num(word: str) -> str:
    my_dict = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    return my_dict[word]

def part_2(file_lines:list) -> int:
    codes = []
    for line in file_lines:
        pattern = r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))'
        line_code = re.findall(pattern, line)
    
        for val in line_code:
            try: 
                int(val)
                
            except ValueError:
                line_code = [convert_words_to_num(val) if item == val else item for item in line_code]
        codes.append(int(line_code[0]+line_code[-1]))
    return sum(codes)


print('Part One result: ', part_1(lines))
print('Part Two: ', part_2(lines))