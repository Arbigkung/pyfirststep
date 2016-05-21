def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title() 

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

#With optional argument
def get_formatted_name(first_name, last_name, middle_name=''):
    
    if middle_name:
        full_name = first_name + ' ' +  middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

my_name = get_formatted_name('biggy', 'pawat', 'de')
print(my_name)
my_name = get_formatted_name('biggy', 'pawat')
print(my_name)

# return dictionary
def build_person(first_name, last_name, age=''):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

name = build_person('jim', 'gordon', age=40)
print(name)
