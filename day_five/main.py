from inspect import walktree


with open('example_part1.txt') as ifile:
    lines=ifile.read().splitlines()

def get_range_overlap(list1: list, list2: list) -> list:
    print(list1,list2)
    overlap_seeds=range(max(list1[0], list2[1]), min(list1[0]+list1[-1], list2[1]+list2[-1])+1)
    print('yes', overlap_seeds)
    return [i for i in overlap_seeds]

def get_int_list(in_lst:list) -> list:
    out_lst=[]
    for lst in in_lst:
        try:
            out_lst.append([int(x) for x in lst.split()])
        except ValueError:
            lst=lst.split(':')[-1]
            out_lst.append([int(x) for x in lst.split()])
    return out_lst

def get_new_seed(list1: list, seeds: list) -> int:
    n=0
    for seed in seeds[::2]:
        
        for lst in list1:
            if get_range_overlap([seed,seed[n+1]], lst)!=[]:
       # print(lst)

      #  print(seed,range(lst[1],lst[1]+lst[-1]))
        if seed in range(lst[1],lst[1]+lst[-1]):
            new_seed=lst[0]+seed-lst[1]
            return new_seed
        else:
            new_seed=seed
    return new_seed

def modify_list(list1: list, list2: list) -> list:
    for lst in list2:
        for i in range(lst[-1]):
            idx_start=lst[1]
            list1[idx_start+i] = lst[0]+i
    return list1

blnk=0
m=0
for n,line in enumerate(lines):
    if line=='':
        if blnk==0:
            seeds=get_int_list(lines[m:n])[0]
           # seed=[int(x) for x in seed.split()]
            blnk+=1
            m=n
        elif blnk==1:
            soil=get_int_list(lines[m+2:n])
            blnk+=1
            m=n
        elif blnk==2:
            fertilizer=get_int_list(lines[m+2:n])
            blnk+=1
            m=n
        elif blnk==3:
            water=get_int_list(lines[m+2:n])
            blnk+=1
            m=n
        elif blnk==4:
            light=get_int_list(lines[m+2:n])
            blnk+=1
            m=n
        elif blnk==5:
            temperature=get_int_list(lines[m+2:n])
            blnk+=1
            m=n
        elif blnk==6:
            humidity=get_int_list(lines[m+2:n])
            blnk+=1
            m=n
    else: 
        location=get_int_list(lines[m+2::])

#for seed in seeds:
real_seeds=[]
#seeds=seeds[0]
# n=0
# for seed in seeds[::2]:
#     n+=2
soil_seed=[]
fert_seed=[]
water_seed=[]
light_seed=[]
temperature_seed=[]
humidity_seed=[]
location_seed=[]
#n=0
#for seed in seeds[::2]:#seeds:
soil_seed.append(seeds,soil)
        #new_seeds=get_range_overlap([seed,seeds[n+1]],list)
    #n+=2
print(soil_seed)
#   #  print(seed)
    #soil_seed.append(get_new_seed(soil,seed))
    print('Done seed')
for seed in soil_seed:
    fert_seed.append(get_new_seed(fertilizer,seed))
    print('Done soil')
for seed in fert_seed:
    water_seed.append(get_new_seed(water,seed))
    print('Done water')
for seed in water_seed:
    light_seed.append(get_new_seed(light,seed))
    print('Done light')
for seed in light_seed:
    temperature_seed.append(get_new_seed(temperature,seed))
    print('Done temp')
for seed in temperature_seed:
    humidity_seed.append(get_new_seed(humidity,seed))
    print('Done humidity')
for seed in humidity_seed:
    location_seed.append(get_new_seed(location,seed))
    print('Done location')




#print(soil_seed,fert_seed,water_seed,light_seed,temperature_seed,humidity_seed,location_seed)

print('Part One: ', min(location_seed))


# my_seed=list(range(100))
# print('WATER', water)
# #print(seed,soil,fertilizer,water,temperature,humidity,location)
# my_seed=modify_list(my_seed,soil)
# soil=my_seed.copy()
# #print(soil,'soil')
# new_fertilizer=modify_list(my_seed, fertilizer)
#new_fertilizer=modify_list(new_soil, fertilizer)
# fert=new_fertilizer.copy()
# new_water=modify_list(my_seed, water)#(new_fertilizer, water)
# wat=new_water.copy()
# print(fert[79])
# # new_light=modify_list(new_water, light)
# # lig=new_light.copy()
# # new_temperature=modify_list(new_light, temperature)
# # temp=new_temperature.copy()
# # new_humidity=modify_list(new_temperature, humidity)
# # hum=new_humidity.copy()
# # new_location=modify_list(new_humidity, location)
# seed=seed[0]
# my_seed_soil=[soil[idx] for idx in seed]
# my_seed_fert=[fert[idx] for idx in seed]
# my_seed_wat=[wat[idx] for idx in seed]
# print(my_seed_wat)
# # my_seed_wat=[wat[idx] for idx in seed[0]]
# # my_seed_lig=[lig[idx] for idx in my_seed_wat]
# # my_seed_tmp=[temp[idx] for idx in my_seed_lig]
# # my_seed_hum=[hum[idx] for idx in my_seed_tmp]
# # my_seed_loc=[new_location[idx] for idx in my_seed_hum]
# print(my_seed_soil,my_seed_fert,my_seed_wat)
