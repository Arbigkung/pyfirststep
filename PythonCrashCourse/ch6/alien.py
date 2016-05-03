alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

#Adding new key-value pairs 
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#Start with empty dictionary

alien_1 = {}

alien_1['color'] = 'green'
alien_1['points'] = 5

print(alien_1)

#Modifying Dictionary values
print("The alien is " + alien_1['color'] + ".")

alien_1['color'] = 'yellow'
print("The alien is now " + alien_1['color'] + ".")

alien_1 = {'x_position': 0, 'y_positon': '25', 'speed': 'medium'}
print("Original x-position: " + str(alien_1['x_position']))

if alien_1['speed'] == 'slow':
    x_increment = 1
elif alien_1['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_1['x_position'] = alien_1['x_position'] + x_increment

print("New x-position: " + str(alien_1['x_position']))

#Remove key-value pairs

alien_2 = {'color': 'green', 'points': 5}
print(alien_2)

del alien_2['points']
print(alien_2)
