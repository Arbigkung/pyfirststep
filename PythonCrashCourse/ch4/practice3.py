#Slices
my_foods = ['pizza', 'falafel', 'carrot cake', 'connoli', 'ice cream']

print(my_foods[0:3])

for my_food in my_foods[:3]:
    print(my_food)

print(my_foods[1:4])

for my_food in my_foods[1:4]:
    print(my_food)

print(my_foods[2:5])

for my_food in my_foods[2:5]:
    print(my_food)

#copy a list
pizzas = ['magarita', 'hawaii', 'super meat delurx']

friend_pizzas = pizzas[:]

pizzas.append('perperoni')

friend_pizzas.append('tuna')
for pizza in pizzas:
    print("My fab pizza is "+ pizza)

for friend_pizza in friend_pizzas:
    print("My friend fab pizza is " + friend_pizza)
