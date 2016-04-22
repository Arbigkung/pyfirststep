#Normal guest list
guest_list = ['mix', 'yut', 'new']

print ("I invited " + guest_list[0].title() + " to my party")
print ("I invited " + guest_list[1].title() + " to my party")
print ("I invited " + guest_list[2].title() + " to my party")

#Changing guest list
guest_list = ['mix', 'yut', 'new']

print ("I invited " + guest_list[0].title() + " to my party")
print ("I invited " + guest_list[1].title() + " to my party")
print ("I invited " + guest_list[2].title() + " to my party")

guest_list.insert(0 , 'art')
print (guest_list)

guest_list.insert(2, 'krit')

print ("Second inv: I invited " + guest_list[0].title() + " to my party")
print ("Second inv: I invited " + guest_list[2].title() + " to my party")

#Add more guest list
guest_list = ['mix', 'yut', 'new']

guest_list.insert(0 , 'art')
guest_list.insert(2 , 'krit')

guest_list.insert(0 , 'taew')
print(guest_list)

guest_list.insert(3, 'june')
guest_list.append('prew')

print ("Third inv: I invited " + guest_list[0].title() + " to my party")
print ("Third inv: I invited " + guest_list[3].title() + " to my party")
print ("Third inv: I invited " + guest_list[6].title() + " to my party")

#Shrinking Guest list
print(guest_list)
guest_list.pop(0)
print(guest_list)
guest_list.pop()
print(guest_list)
guest_list.pop()
guest_list.pop()
print(guest_list)
del guest_list[3]
del guest_list[2]
print(guest_list)
