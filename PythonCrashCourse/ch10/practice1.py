#learning python
file_path = 'input/learning_python.txt'

#Read whole file
with open(file_path) as file_object:
    contents = file_object.read()
    print(contents)

#Read line
with open(file_path) as file_object:
    for line in file_object:
        print(line.rstrip())

#List line and print at other block
with open(file_path) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

#Learning C, why it's not working?!
with open(file_path) as file_object:
    content = file_object.readline()
    content.replace('python', 'c')
    print(content)
