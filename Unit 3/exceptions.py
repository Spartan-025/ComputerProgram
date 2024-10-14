
def add_2():
    try:
        x = int(input("What is the first number?\n"))
        y = int(input("What is second?\n"))
        print(x+y)

    except:
        print("Invaled entry")
        add_2()

add_2() 



def divid_2():
    try:
        x = int(input("What is the first number?\n"))
        y = int(input("What is second?\n"))
        print(x/y)

    except ValueError:
        print("Please enter a whole number.")
        divid_2()

    except ZeroDivisionError:
        print("Can not divid by zero.")
        divid_2()

divid_2() 