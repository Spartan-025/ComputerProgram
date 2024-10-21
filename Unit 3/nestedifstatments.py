
prime = True 
cost = 20
age = 17 
consent = False 

if prime:
    if age >= 18:
        print("You are eligable for free shipping.")
    else:
        if consent:
            print("You can have free shipping.")
        else:
            print("No free shipping.")

elif cost >=25:
    if age>=18:
        print("Free shipping")
    elif consent:
        print("Free shipping")
    else:
        print("No free shipping")
else:
    print("No free shipping")
