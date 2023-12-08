import numpy as np
with open('input.txt') as ifile:

    input=ifile.read().splitlines()

def get_distance(hold_time: int, time: int) -> int:
    speed=hold_time*1
    return speed*(time-hold_time)
time = [int(x) for x in (input[0].split(':')[1:])[0].split()]
distance = [int(x) for x in (input[1].split(':')[1:])[0].split()]

winning_per_race=[]
err_margin=[]
for t, d in zip(time, distance):
    win=[]
    for ms in range(1,t+1):
        if get_distance(ms, t) > d:
            win.append(ms)
    winning_per_race.append(win)
    err_margin.append(len(win))
#print(t,d, type(t))
#time=time[0].split()
print(np.prod(err_margin))

##PART TWO
err_margin2=[]
time = int(input[0].split(':')[1:][0].replace(' ',''))
distance = int(input[1].split(':')[1:][0].replace(' ',''))
print(range(1,time+1))
win=[]
for t in range(1,time+1):

    if get_distance(t, time) > distance:
        #print('true', t)
        win.append(t)
        #print(win)
err_margin2.append(len(win))

print(np.prod(err_margin2))
