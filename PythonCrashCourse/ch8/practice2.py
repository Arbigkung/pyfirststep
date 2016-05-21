#T-Shirt with large size is default
def make_shirt(text, size = 'L'):
    print("\nYour order shirt size " + size )
    print("Your text: " + text)

make_shirt('Hello Jorgh!', 'M')
make_shirt(size = 'M', text = 'May the force')
make_shirt(text = 'I love Python')

#Cities
def describe_city(city, country = 'US'):
    print("\n" + city + " is in " + country)

describe_city('Bangkok', 'Thailand')
describe_city(city = 'Taipei', country = 'Taiwan')
describe_city('Jorgh Town')
