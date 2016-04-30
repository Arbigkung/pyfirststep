#Tuple
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

#Shouldn't work
#dimensions[0] = 250

for dimension in dimensions:
    print(dimension)

print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
#Edit tuple need to redefinde entire tuple
dimensions = (400, 100)

print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

