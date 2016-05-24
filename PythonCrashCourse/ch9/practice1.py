#Resturant

class Restaurant(object):
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
    
    def describe_restaurant(self):
        print("This restaurant name is " + self.name.title())
        print("Cuisine type is " + self.type.title())
    
    def open_restaurant(self):
        print(self.name.title() + " is open.")

my_rest = Restaurant('Biggy hut', 'Thaifood')
print(my_rest.name.title())
print(my_rest.type.title())

my_rest.describe_restaurant()
my_rest.open_restaurant()

#User

class User(object):
    def __init__(self, first_name, last_name):
        self.name = first_name
        self.sakul = last_name
    
    def describe_user(self):
        print("User's name is " + self.name.title())
        print("User's last name is " + self.sakul.title())
    
    def greet_user(self):
        print("Hello, " + self.name.title() + " " + self.sakul.title())

my_info = User('Pawat', 'Soodlor')
print(my_info.name)
print(my_info.sakul)
my_info.describe_user()
my_info.greet_user()
