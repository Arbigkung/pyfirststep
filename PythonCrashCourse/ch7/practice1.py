#Rental car
car = raw_input("What kind of car you like?: ")
print("Let me see if I can find you a " + car.title())

#Restaurant Seating
p_number = raw_input("How many people are in your group?: ")
p_number = int(p_number)

if p_number > 8:
    print("Please waiting for your seat.")
else:
    print("Your seat is ready.")

#Multiple of ten
number = raw_input("Type your number and I will show you it is multiple of ten or not")
number = int(number)

if number % 10 > 0:
    print("Your number is not multiple of ten")
else:
    print("Your number is multiple of ten")
