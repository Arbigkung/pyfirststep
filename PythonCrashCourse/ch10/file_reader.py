file_path = 'input/pi_digits.txt'

#Read whole file
with open(file_path) as file_object:
    contents = file_object.read()
    print(contents)

#Read line by line
with open(file_path) as file_object:
    for line in file_object:
        print(line.rstrip())

#List line and print at other block
with open(file_path) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())


