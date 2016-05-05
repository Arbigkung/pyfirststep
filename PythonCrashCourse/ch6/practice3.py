#Person
person1 = {
    'first_name': 'Pawat', 
    'nick_name': 'Big', 
    'age': 26, 
    'city': 'Bangkok'
    }
person2 = {
    'first_name': 'Warat', 
    'nick_name': 'Boom', 
    'age': 21, 
    'city': 'Bangkok'
    }
person3 = { 
    'first_name': 'Nuttawut',
    'nick_name': 'Mix',
    'age': 25,
    'city': 'Samutprakarn'
    }
persons = [person1, person2, person3]

for person in persons:
  print("Name: " + person['first_name'] + " Nick name: " + person['nick_name'] + " age: " + str(person['age']) + "  city: " + person['city'])

#Pet
pet1 = {
    'mumu': {
        'kind': 'dog',
        'owner': 'big',
        }
    } 

pet2 = {
    'mew': {
        'kind': 'cat',
        'owner': 'boom',
        }
    }

pet3 = {
    'jiew': {
        'kind': 'mouse',
        'owner': 'mam',
        }
    }

pets= [pet1, pet2, pet3]

for pet in pets:
    for name, info in pet.items():
        print("Pet name is " + name)
        print("It is " + info['kind'] + " and owner is " + info['owner'])

#Fav place
fav_places = {
    'mix': ['japan', 'indonesia', 'hongkong'],
    'yut': ['home', 'siam square'],
    'big': ['bangkok', 'taipei', 'singapore'],
    }

for name, places in fav_places.items():
    print (name.title() + " favourite place is :")
    for place in places:
        print('\t' + place)

#Fav num
fav_num = {}
fav_num['big'] = [8,9]
fav_num['boom'] = [7,8]
fav_num['pa'] = [9]
fav_num['ma'] = [1,8]
fav_num['arma'] = [5]

for name, numbers in fav_num.items():
    print(name + "'s favourite number is:")
    for number in numbers:
        print("\t" + str(number))

#cities
cities = {
    'Bangkok':
        {
        'country': 'Thailand',
        'population': '5 M',
        'places': ['wat parkaew', 'chaopraya river']
        },
    'Taipei':
        {
        'country': 'Taiwan',
        'population': '6 M',
        'places': ['Taipei 101', 'Dan sui', 'Mao kong'] 
        },
    'Singapore':
        {
        'country': 'Singapore',
        'population': '10 M',
        'places': ['Garden by the bay', 'Merlion', 'Sentosa']
        }
}

for city, info in cities.items():
    print("City name " + city)
    print("Is part of " + info['country'])
    print("Number of people is " + info['population'])
    print("Famous place is:")
    for place in info['places']:
        print("\t" + place)
        

