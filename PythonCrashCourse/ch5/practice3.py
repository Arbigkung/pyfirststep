#Hello admin
users = ['big', 'boom', 'admin', 'pa', 'ma']

for user in users:
    if user == 'admin':
        print("F**, " + user.title())
    else:
        print("Hello, " + user.title())

#No users
users = []

if users:
    for user in users:
        if user == 'admin':
            print("F**, " + user.title())
        else:
            print("Hello, " + user.title())
else:
    print("Yoou need to find some user!")

#Checking Users

users = ['big', 'boom', 'admin', 'pa', 'ma']
new_users = ['art', 'mix', 'big', 'boom', 'yut']

for new_user in new_users:
    if new_user.lower() in users:
        print("Username : " + new_user + " is unavailable")
    else: 
        print("You can use " + new_user + " as a username")

#Ordinal Number
numbers = list(range(1,10))

for number in numbers:
    if (number == 1):
        print(str(number) + "st\n")
    elif (number == 2):
        print(str(number) + "nd\n")
    elif (number == 3):
        print(str(number) + "rd\n")
    else:
        print(str(number) + "th\n")
