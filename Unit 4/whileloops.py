#In programming, loops are essential tools that help repeat sections of code without
#manually writing the same instructions multiple times.
#One of the most common types of loops in Python is the while loop. 
#Understanding how while loops work is 
#fundamental for tasks that involve repeated actions based on conditions.

real_pass = "potato45"
entered_pass = ""
attempts = 0
while real_pass != entered_pass:
    entered_pass = input("Please enter the password\n")
    attemps = attempts + 1
    if entered_pass == real_pass:
        print("POTATO IN")
    else:
        print("Potato say no")
        print("You are on your " + str(attempts) + " try")
    
#Infinet loop - no good
count = 0
while True:
    count += 1011010101
    print(count)