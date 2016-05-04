favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

print("Sarah's favourite language is " + favourite_languages['sarah'].title() + ".\n")

#use for loop to go through key-value
for name, language in favourite_languages.items():
    print(name.title() +  "'s favourite language is " + language.title() + ".\n")

#looking just key
for name in favourite_languages.keys():
    print(name.title())

#looking though dictionary key in order
for name in sorted(favourite_languages.keys()):
    print(name.title() + ", thank you for thking the poll.")

#looking all value in a dictionary
print("The following languages have been mentioned:")
for language in favourite_languages.values():
    print(language.title())

#looking unique value data
print("The following languages have been mentioned:")
for language in set(favourite_languages.values()):
    print(language.title())
