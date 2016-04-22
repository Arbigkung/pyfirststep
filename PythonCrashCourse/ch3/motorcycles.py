motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

#Pop out item from list
last_owned = motorcycles.pop()
print "My last owned motorcycle is " + last_owned.title()

print(motorcycles) 

#Pop out item from any Position in a list
first_owned = motorcycles.pop(0)
print "My first owned motorcycle is " + first_owned.title()

print(motorcycles)

#Remove item by Value
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']

expensive = 'ducati'
motorcycles.remove(expensive)
print(motorcycles)
print("\nA " + expensive.title() + " is too expensive for me.")
