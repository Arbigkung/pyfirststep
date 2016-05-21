# Make great
def make_great(magicians, great_magicians):
    for magician in magicians:
        name = "Greate " + magician
        great_magicians.append(name)

# Magicians
def show_magicians(magicians):
    for magician in magicians:
        print(magician + " is show")

great_magicians = []
magicians = ['david', 'big', 'openhem']

make_great(magicians[:], great_magicians)
show_magicians(great_magicians)
show_magicians(magicians)

