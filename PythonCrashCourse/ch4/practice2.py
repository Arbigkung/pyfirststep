for value in range(1,21):
    print value

#Sum one million
million = []
for value in range(1,1000001):
    million.append(value)
#or 
#million = list(range(1,1000001))

mini = min(million)
maxi = max(million)
sumi = sum(million)

print(mini) 
print(maxi)
print(sumi)

#Odd number
odd_nums = list(range(1,21,2))

for odd_num in odd_nums:
    print(odd_num)

#Three
three_nums = list(range(3,31,3))

for three_num in three_nums:
    print(three_num)

#Cube
cubes = []

for value in range(1,11):
    cubes.append(value**3)

for cube in cubes:
    print(cube)

#Cube comprehension
com_cubes = [value**3 for value in range(1,11)]

for com_cube in com_cubes:
    print(com_cube)
