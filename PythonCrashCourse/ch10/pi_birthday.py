filename = 'input/pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

birthday = raw_input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appear in the first million digits of pi!")
else: 
    print("Your are no luck!")
