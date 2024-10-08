print ("Here is your Simple Quiz!")

ans_1 = int(input("What is 5 + 5?\n"))

ans_2 = int(input("How many legs does a spider have?\n"))

ans_3 = float(input("If you have $12.50 with you and you buy something that is worth $8.25, how much do you have left?\n"))

ans_4 = float(input("What is the area of a circle that has a diamiter of 6 (round to the tenth)?\n"))

ans_5 = int(input("What was the answer to the first question?\n"))

def tally_score():
    score = 0
    
    if ans_1 == int(10):
        score = score +1 

    if ans_2 == int(8):
        score = score +1

    if ans_3 == float(4.25):
        score = score +1

    if ans_4 == float(9.4):
        score = score +1

    if ans_5 == int(10):
        score = score +1

    print("Your score out of five is")
    print(score)
   
tally_score()