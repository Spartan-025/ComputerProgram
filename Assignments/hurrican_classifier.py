wind = input("How fast are the winds of the storm?(Just the number)\n>")

if wind() < 74:
    print("It is just a tropical storm.")

elif wind() < 96:
    print("It is a category 1 hurrican.")

elif wind() < 111:
    print("It is a category 2 hurrican.")

elif wind() < 130:
    print("It is a category 3 hurrican.")

elif wind() < 157:
    print("It is a category 4 hurrican.")

else:
    print("It is a catigory 5 hurrican!")