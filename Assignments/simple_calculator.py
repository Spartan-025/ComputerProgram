print("This is your simple calculator that can")
print("add, subtract, multiply and divide any numbers you want!")
print(" ")

def add():                                                       # Adding the numbers the user gives
    print("Add two numbers:")
    x = int(input("What is the first number?\n"))
    y = int(input("what is the second number?\n"))
    print(str(x) + " + " + str(y) + " = " + str(x + y)) 

add()

def subtract():                                                  # Subtracting the numbers the user gives
    print("Subtract two numbers:")
    x = int(input("What is the first number?\n"))
    y = int(input("what is the second number?\n"))
    print(str(x) + " - " + str(y) + " = " + str(x - y)) 

subtract()

def multiply():                                                  # Multiplying the numbers the user gives
    print("Multiply two numbers:")
    x = int(input("What is the first number?\n"))
    y = int(input("what is the second number?\n"))
    print(str(x) + " * " + str(y) + " = " + str(x * y)) 

multiply()

def divide():                                                  # Dividing the numbers the user gives
    print("Divide two numbers:")
    x = int(input("What is the first number?\n"))
    y = int(input("what is the second number?\n"))
    print(str(x) + " / " + str(y) + " = " + str(x / y)) 

divide()