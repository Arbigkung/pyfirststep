#glossary 2
slangs = {
    'lumyai': 'too much',
    'yome': 'too hot and waiting to long',
    'nok': 'miss'
    }
for key, value in slangs.items():
    print(key + " is means: " + value)

#river
rivers = {
    'chaopraya': 'bangkok',
    'maekhong': 'laos',
    'xindian': 'taipei',
    'yangxi': 'beijing',
    }

for river, country in rivers.items():
   print(river.title() + " is at " + country.title())

for river in rivers.keys():
   print(river.title())

for country in rivers.values():
   print(country.title())

#polling
favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
friends = ['jen', 'sarah', 'edward', 'phil', 'mix']

for friend in friends:
    if friend in favourite_languages.keys():
        print("Thank you " + friend + " for taking poll")
    else:
        print("Hey " + friend + " can you help me to make poll?")

