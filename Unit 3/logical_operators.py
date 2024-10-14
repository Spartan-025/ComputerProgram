
#Comparison operators  < > == <= >=
#Arithmetic operators  + - / * % ** // 

def comp_el(age, exp):
    if age >= 18 and exp >= 3:
        print("You can enter the comp.")

    elif age < 18:
        print("You are too young")

    elif exp < 3:
        print("Yound don't have enugh experience.")

    else:
        print("You can't enter the comp.")

a = int(input("How old are you?"))
e = int(input("How many yoears of experience do you have?"))

comp_el(a, e)

#Advanced Logical Operators - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

#Amazon free shipping el
#prime customer OR purchases of over $25
#Under 18, need parent consent to purchase

def free_ship(prime, cost, age, consent):
    if (prime == True or cost >= 25) and (age >= 18 or consent == True):
        print("Free shipping applied!")
    else:
        print("No free shipping for you")

p = True
cos = 18 
a = 12 
con = True

free_ship(p, cos, a, con)