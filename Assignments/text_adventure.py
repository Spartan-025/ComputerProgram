#The start of the story, give backround information about the adventure
def start_of_the_adventure():
    print("You are in the 17th Airborne Division or The Golden Talons")
    print("The date is January 3rd, 1945")
    print("DAY 1: DAY BEFORE THE MISSION")
start_of_the_adventure()
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
        day1_the_decision()
def go_on_mission():
    print("You have decided to go, you start flying out tonight.")
    day2_the_jump()
def dont_go():
    print("You were arrested for insubordination.\nGAME OVER")
#The second choice, leads to if you jump early, you could live, if you stay for longer you have a chance of get shot down.
def day2_the_jump():
    print("DAY 2: THE JUMP\nJannuary 4th, 1945, it is 8:00. The drop time is 8:15.")
    print("You are almost to the drop point, nerves are getting to you. you have done over 100 drops, but this one feels diffrent.")
    print("8:15, the pilot says he wants to go a little further before the jump, but you where told to stay on the mission.")
    print("1. Stay on the plane and jump somewhere else\n2. Tell your team to jump now")
    the_jump = input("> ")
    if the_jump == "2":
        jump_now() 
    elif the_jump == "1":
        wait_to_jump()
    else:
        print("Decide by using 1 or 2")
        day2_the_jump()
def jump_now():
    print("8:23, you and your team have just landed and are packing up your parachutes")
    day2_boots_down()
def wait_to_jump():
    print("8:23, you here flack and AA guns shooting. Gun fire lights up the sky all around you.")
    import random 
    r = random.random()
    if r < 0.50:
        print("The wing of the plane has been cliped, you and your team need to jump now.")
        day2_outside_dp()
    else:
        print("The plane was shot down and crashed.\nGAME OVER")
#The 3rd encounter, deciding where to go.
def day2_boots_down():
    print("You and your team landed in the drop zone. The plan is to move to the North and push up to the front lines.")
    print("But there is a town 10 miles to the North-East, and to the West there is a known Axis artillerly base.")
    print("1. Go North\n2. Go North-East to the town\n3. Go West to the Axis base")
    where_march = input("> ")
    if where_march == "1":
        print("You and your team are marching North")
        day2_march_north()
    elif where_march == "2":
        print("You decided to go to the town.")
        day2_the_town()
    elif where_march == "3":
        print("You are going to a known enemy base")
        day2_go_to_axis_artillery_base()
    else:
        print("Decide using 1,2 or 3")
        day2_boots_down()
#If you surrvive the plane you are here, another encounter
def day2_outside_dp():
    print("You landed East of the drop point by 5 miles. There is a town just North of you position.")
    print("1. Go to the town\n2. Go around the town to the front lines")
    where_going_from_outside_dp = input("> ")
    if where_going_from_outside_dp == "1":
        print("You are going to the town")
        day2_the_town()
    elif where_going_from_outside_dp == "2":
        print("You are going around the town to the front lines.")
def day2_march_north():
    print("You decided to march North with your battalion.\n21:42, you have been marching all day and the solders want to stop for the night.")
    print("1. Make camp and stay the night\n2. Keep marching")
def day2_go_to_axis_artillery_base():
    print("11:25, you are almost to the Axis base.\nYou have came up with 2 plans to attack.")
    print("1. Go all in with a frontal assault\n2. Split into 2 teams and attack from the North and South.")
    axis_artillery_assault = input("> ")
    if axis_artillery_assault == "1":
        print("11:53, you see the Axis forces.")
    elif axis_artillery_assault == "2":
        print("")
    else:
        print("Decide by using 1 or 2")
        day2_go_to_axis_artillery_base()
def day2_the_town():
    print("You are headed to the town.\n9:13, you are entering the town, it looks deserted.")
    print("You are walking down the road and suddenly you see 2 Axis solders walk around the corner.")
    print("1. Do you open fire at them\n2. Do you tell your squad to hide")
    the_2_solders = input("> ")
    if the_2_solders == "1":
        print("You and your team open fire at the solders, both of the enemy solders are down and your team doesn't any injurys.")
        day2_town_battle()
    elif the_2_solders == "2":
        print("Your squad hid behind the corner of a building, you see the solders walk away from you.")

def day2_town_battle():
    print("9:37, it is silent. The Axis solders bodies are laying in the middle of the road")
    print("You hear people running, the sound of magazines clanking and helmets hitting against weapons.")
    print("Suddenly you see 40 or more Axis solders running down the road")
    print("Bullets started flying, solders from both sides started yelling and falling")
    print("You are pinned down in gunfire for hours\n15:18, the gunfire has died down, it is silent.")
    print("You look around, there are only 16 other solders around you. You rally them up and go into a building adjacent to you.")
    print("1. Do you stay in the building until the morning\n2. Do you go out and keep serching the town")
    day2_in_the_building = input("> ")
    if day2_in_the_building == "1":
        print("")
    elif day2_in_the_building == "2":
        print("")
    else:
        print("Decide using 1 or 2")
        day2_town_battle()


day1_the_decision()

