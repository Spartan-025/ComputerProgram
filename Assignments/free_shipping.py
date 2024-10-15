
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