#Break, continue, and pass
#Break exits a loop

bag_fruit = ["apple", "strawbery", "bug", "pear", "watermelon"]

for fruit in bag_fruit:
    print("You ate a " + fruit)

    if fruit == "bug":
        print("You found a bug in the bag")
        break 
    else:
        print("You ate a" + fruit)

#Continue skips the current loop


#Dictionarys they use the currly braces
me = {
    "name" : "Caden",
    "age" : 15,
    "city" : "St. Michael",
    "pets" : 1,
}
#each key has to be unique

print(me["age"])
print(me.get("height"))

#Remove entries
me.pop("pets")
#dictanary tools
print(me.keys()) #returns all keys
print(me.values())#returns all values   
print(me.items())#returns all pairs
print(me.clear())#removes evrythis / clears it