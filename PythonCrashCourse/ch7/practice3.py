# Deli 
sandwich_orders = ['Chicken', 'Tongkasu', 'Tuna', 'Salmon']
finished_sandwiches = []

while sandwich_orders:
    current_order = sandwich_orders.pop()
    print("I made " + current_order + " sandwich for you\n")
    
    finished_sandwiches.append(current_order)

for finished_sanwich in finished_sandwiches:
    print("You " + finished_sanwich +" sanwich is ready to serve")

# No pastrami
sandwich_orders = ['Chicken','pastrami', 'pastrami', 'Tongkasu', 'Tuna', 'Salmon', 'pastrami']
finished_sandwiches = []

print("No pastrami today! \n")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print(sandwich_orders)

# Dream Vacation
dream_lists = {}
active = True

while active:

    name = raw_input("Please enter your name\n")
    place = raw_input("Please enter you dream destination\n")

    dream_lists[name] = place

    choice = raw_input("You want to add dream list for other person? (yes/no)\n")
    
    if choice == 'no':
        active = False

for name, place in dream_lists.items():
    print(name + " want to go " + place)
