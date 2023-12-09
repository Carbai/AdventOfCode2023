def parse_input(filename: str) -> list:
    with open(filename) as ifile:
        lines=ifile.read().splitlines()
        seq=[]
        for line in lines:
            seq.append([(int(x)) for x in line.split()])
        return seq

def get_diff(numbers: list) -> int:
    stop=False
    next_n=[numbers[-1]]
    tmp=[]
    curr_numbers=numbers[:]
    while not stop:
        for i,n in enumerate(curr_numbers[1::]):
            tmp.append(n-curr_numbers[i])
        next_n.append(tmp[-1])
        curr_numbers=tmp
        if all(x==0 for x in curr_numbers):
            stop=True
        tmp=[]
    return sum(next_n)

def part_one(sequences:list):
    result=[]
    for seq in sequences:
        result.append(get_diff(seq))
    return sum(result)








def get_diff2(numbers: list) -> list:
    stop=False
    next_n=[]
    tmp=[]
    curr_numbers=numbers[:]

    while not stop:
        for i,n in enumerate(curr_numbers[1::]):
            tmp.append(n-curr_numbers[i])
        next_n.append(tmp[0])
        curr_numbers=tmp
        if all(x==0 for x in curr_numbers) or len(curr_numbers)==1:
            stop=True
        tmp=[]
    return next_n

def result_reduction(num: list) -> int:
    num=num[::-1]
    while len(num)!=1:
        num[1]=num[1]-num[0]
        num=num[1:]
    return num[0]

SEQUENCES=parse_input('input.txt')

def part_two(sequences: list):
    tot=0
    for seq in sequences:
        result=get_diff2(seq)
        res=result_reduction(result)
        tot+=seq[0]-res
    
    return tot
  #  part_two.append(seq[0]-result_reduction(result2))

#print('Part one: ', part_one(SEQUENCES))
print('Part two: ', part_two(SEQUENCES))