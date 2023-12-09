def parse_input(filename: str) -> list:
    with open(filename) as ifile:
        lines=ifile.read().splitlines()
        seq=[]
        for line in lines:
            seq.append([(int(x)) for x in line.split()])
        return seq

SEQUENCES=parse_input('input.txt')

def get_diff(numbers: list, idx_target=int) -> int:
    stop=False
    if idx_target==0:
        next_n=[]
    elif idx_target==-1:
        next_n=[numbers[idx_target]]
    tmp=[]
    curr_numbers=numbers[:]
    while not stop:
        for i,n in enumerate(curr_numbers[1::]):
            tmp.append(n-curr_numbers[i])
        next_n.append(tmp[idx_target])
        curr_numbers=tmp
        if all(x==0 for x in curr_numbers):
            stop=True
        tmp=[]
    return next_n

def part_one(sequences:list):
    result=[]
    for seq in sequences:
        result.append(sum(get_diff(seq, -1)))
    return sum(result)

def result_reduction(num: list) -> int:
    num=num[::-1]
    while len(num)!=1:
        num[1]=num[1]-num[0]
        num=num[1:]
    return num[0]

def part_two(sequences: list):
    tot=0
    for seq in sequences:
        result=get_diff(seq,0)
        res=result_reduction(result)
        tot+=seq[0]-res
    return tot

print('Part one: ', part_one(SEQUENCES)) ##1938800261
print('Part two: ', part_two(SEQUENCES)) ##1112