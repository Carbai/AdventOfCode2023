import numpy as np
import math
with open('input.txt') as ifile:
    input=ifile.read().splitlines()

time = int(input[0].split(':')[1:][0].replace(' ',''))
distance = int(input[1].split(':')[1:][0].replace(' ',''))

minim=math.ceil(distance/time)
lst = [i for i in range(minim,time-minim)]
n=lst[0]

print(time, distance, minim, time-minim)

