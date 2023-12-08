from cmath import pi

def get_data(data:list, start:str) -> list:
    out_list=[]
    n=data.index(start)
    for line in data[n+1:]:
            if line != '' and n!= len(data):
                out_list.append(line)
                n+=1
            else:
                return out_list
    return out_list
            
            
def get_range(row_data: list) -> tuple:
    actual_range=[]
    map_range=[]
    for row in row_data:
        row=[int(x) for x in row.split()]
        actual_range.append(range(row[1],row[1]+row[-1]))
        map_range.append(range(row[0],row[0]+row[-1]))
    return (actual_range, map_range)

def parse_input(filename):
    with open(filename) as ifile:
        lines=ifile.read().splitlines()
        seeds=[int(x) for x in lines[0].split(':')[-1].split()]
        seeds_ranges=[]
        for seed in seeds[::2]:
            print(seed,seeds.index(seed))
            seeds_ranges.append(range(seed,seed+seeds[seeds.index(seed)+1]))
        soil = get_range(get_data(lines, 'seed-to-soil map:'))
        fertilizer=get_range(get_data(lines, 'soil-to-fertilizer map:'))
        water=get_range(get_data(lines,'fertilizer-to-water map:'))
        light=get_range(get_data(lines,'water-to-light map:' ))
        temperature=get_range(get_data(lines, 'light-to-temperature map:'))
        humidity=get_range(get_data(lines, 'temperature-to-humidity map:'))
        location=get_range(get_data(lines, 'humidity-to-location map:'))
    return(seeds_ranges,soil,fertilizer,water,light,temperature,humidity,location)

print(parse_input('example_part1.txt'))