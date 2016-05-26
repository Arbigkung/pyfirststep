#Ice Cream Stand
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

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type='dessert'):
        super(IceCreamStand, self).__init__(restaurant_name, cuisine_type)
        self.flavors = ['chocolate', 'vanilla', 'cookies&cream', 'rum rasine']
    
    def display_flavors(self):
       for flavors in self.flavors:
            print(flavors.title() + ' is available')
    
my_rest = Restaurant('Biggy hut', 'Thaifood')
print(my_rest.name.title())
print(my_rest.type.title())
 
my_rest.describe_restaurant()
my_rest.open_restaurant()
my_rest.set_number_served(20)
print(str(my_rest.number_served))
my_rest.increment_number_served(20)
print(str(my_rest.number_served))

my_ice = IceCreamStand('Biggy Ice')
my_ice.describe_restaurant()
my_ice.display_flavors()

#Admin
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
        
class Admin(User):
    def __init__(self, first_name, last_name):
        super(Admin, self).__init__(first_name, last_name)
        self.priv = Priviledges()        

class Priviledges(object):
    def __init__(self):
        self.priviledges = ['can delete post', 'can ban user', 'can promote user']
    
    def show_priviledges(self):
        for priviledge in self.priviledges:
            print('Admin can ' + priviledge)

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
my_admin = Admin('Biggy', 'Lnw')
my_admin.greet_user()
my_admin.priv.show_priviledges()


