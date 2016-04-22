#Sort method 
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

#Temporaily sort
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

#Reverse sort
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
print("\n")
print(cars)

#Find the length of a list
print("\n")
print(len(cars))
