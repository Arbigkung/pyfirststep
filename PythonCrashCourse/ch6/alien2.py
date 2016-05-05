alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# make 30 aliens!
aliens_l1 = []

for alien_number in range(30):
    new_alien = {'color': 'green', 'point': 5, 'speed': 'slow'}
    aliens_l1.append(new_alien)

for alien in aliens_l1[:5]:
    print(alien)
print("...")

print("Total nuumer of aliens: " + str(len(aliens_l1)))
