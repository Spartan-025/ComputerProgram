#The start of the story, give backround information about the adventure
def start_of_the_adventure():
    print("You are in the 17th Airborne Division or The Golden Talons")
    print("The date is January 3rd, 1945")
    print("DAY 1: DAY BEFORE THE MISSION")
#The first choice, deciding to go or not
def day1_the_decision():
    print("You have been in the 17th Airborne Division for 2 years.")
    print("You have been waiting to be deployed and the time finaly arrived.")
    print("The mission, if you decide to go on, would soon be known as\nDead Man's Ridge.")
    print("Here are your options.\n1. Accept the mission\n2. Refuse getting deployed.")

    deciding = input("> ")

    if deciding == "1":
        go_on_mission()
    elif deciding == "2":
        dont_go()
    else:
        print("Decide by using 1 or 2")
        start_of_the_adventure()

def go_on_mission():
    print("You have decided to go, you start flying out tonight.")
    day2_the_jump()

def dont_go():
    print("You were arrested for insubordination.\nGAME OVER")

#The second choice, leads to if you jump early, you could live, if you stay for longer you get shot down.

def day2_the_jump():
    print("DAY 2: THE JUMP\nJannuary 4th, 1945, it is 8:00. The drop time is 8:15.")
    print("You are almost to the drop point, nerves are getting to you. you have done over 100 drops, but this one feels diffrent.")
    print("")

import random 

r = random.random()
if r < 0.50:
    print("Sucses")
else:
    print("Fail")