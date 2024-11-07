import random
real_num = random.randint(1,101)
enter_num = ""
attempt = 0
def done():
    print("Good job!\nThis is how many attemps you had\n" + str(attempt))
print("There is a number between 1 and 100, guess it.")
while real_num != enter_num:
    enter_num = input("What do you think the number is\n>")
    attempt = attempt + 1 
    if int(enter_num) == real_num:
        print ("You found the number")
        done()
    elif int(enter_num) > real_num:
        print("You are too high")
    elif int(enter_num) < real_num:
        print("You are to low")
    else:
        print("You have to guess using a number")

