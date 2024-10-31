#A list is a way to store more than one value in a varible, they are called ITEMS
#Items can be accessed by their index(position in the list)
#Index starts at 0                  0               1               2               3
best_elden_ring_weapons = ["Blasphemous Blade", "Moonveil", "Rivers of Blood", "Iron Ball"]
best_years = [1776, 1985, 1994, 1957]
print(best_years.index(1985))


#print the best
print(best_elden_ring_weapons[0])

#print the worst of the best
print(best_elden_ring_weapons[len(best_elden_ring_weapons)-1])
#the .pop() removes an item in a list by position
best_elden_ring_weapons.pop(3)
#removes an item by its value / only the first on none after that
best_elden_ring_weapons.remove("Moonveil")
#To add on to / 
best_elden_ring_weapons.append("Mohgwyn's Scared Spear")

print(best_elden_ring_weapons)


import random
numbers = [random.randint(1,100), random.randint(1,100), random.randint(1,100)]
print(numbers)
print(max(numbers))
print(min(numbers))
print(numbers.sort())