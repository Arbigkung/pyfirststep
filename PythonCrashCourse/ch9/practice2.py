#Number Served
class Restaurant(object):
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        #add number of served
        self.number_served = 0

    def describe_restaurant(self):
        print("This restaurant name is " + self.name.title())
        print("Cuisine type is " + self.type.title())

    def open_restaurant(self):
        print(self.name.title() + " is open.")
    
    #number of served method
    def set_number_served(self, number):
        self.number_served = number
    
    #increment number of served
    def increment_number_served(self, number):
        self.number_served += number

my_rest = Restaurant('Biggy hut', 'Thaifood')
print(my_rest.name.title())
print(my_rest.type.title())
 
my_rest.describe_restaurant()
my_rest.open_restaurant()
my_rest.set_number_served(20)
print(str(my_rest.number_served))
my_rest.increment_number_served(20)
print(str(my_rest.number_served))

#User
class User(object):
    def __init__(self, first_name, last_name):
        self.name = first_name
        self.sakul = last_name
        self.attempt = 0

    def describe_user(self):
        print("User's name is " + self.name.title())
        print("User's last name is " + self.sakul.title())
    
    def greet_user(self):
        print("Hello, " + self.name.title() + " " + self.sakul.title())
    
    #increment number of login attempt
    def increment_login_attempt(self):
        self.attempt += 1
    
    def reset_login_attempt(self):
        self.attempt = 0
        
my_info = User('Pawat', 'Soodlor')
print(my_info.name)
print(my_info.sakul)
my_info.describe_user()
my_info.greet_user()
my_info.increment_login_attempt()
print(my_info.attempt)
my_info.increment_login_attempt()
print(my_info.attempt)
my_info.reset_login_attempt()
print(my_info.attempt)
