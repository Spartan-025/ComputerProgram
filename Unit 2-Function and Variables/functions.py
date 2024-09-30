
def add(x, y):
    print(x + y)




print("What are your top five movies?")

movie_1 = input("What is your first\n")
movie_2 = input("What is your second?\n")
movie_3 = input("What is your third\n")
movie_4 = input("What is your fourth?\n")
movie_5 = input("What is your fith?\n")


def your_movies():
    print("1. " + movie_1)
    print("2. " + movie_2)
    print("3. " + movie_3)
    print("4. " + movie_4)
    print("5. " + movie_5)

print("Here are your top five movies!")
your_movies()

x = 4
def my_function():
    global x    #From now on, when I call x, I'm talking about the global version!! Not the local verison...
    x = 5       #Reassigning the global variable x
    print(x)    #Prints 5

print(x)  
my_function()
print(x)


print("What is your item?")
item = input("")
print("How much is it")
price = float(input(""))
rate = float(.06875)

new_price = (price * rate)
full_price = (new_price + price)
print("Your amount is $")
print(full_price)