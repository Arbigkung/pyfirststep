#Pizza Topping
prompt = "\nPlease add you pizza topping"
prompt += ("\nplese enter 'quit' to exit: ")

active = True

while active:
    order = raw_input(prompt)
    
    if order == 'quit':
        active = False
    else:
        print("You order: " + order)

#Movie Ticket
prompt = "\nPlease enter you age to buy ticket"
prompt += "\n(plese enter 'quit' to exit)"

while True:
    order = raw_input(prompt)
    if str(order) == 'quit':
        break
    elif int(order) < 3:
        print("You're free to see movie!")
    elif int(order) >= 3 and int(order) <= 12:
        print("Your ticket price is $10")
    elif int(order) > 12:
        print("Your ticket price is $15")
    
