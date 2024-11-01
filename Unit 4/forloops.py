#allow the programer to repeat, or loop.
#
#for <temp var> in <list>:


for i in range(0,11):
    print(i)


top_food = ["eggs benedict", "fried chicken", "mac n cheese"]

for food in top_food:
    print(food)

groceries = ["milk", "eggs", "bread", "butter", "apples"]
item_added = input("what did you get?\n>")
if item_added.lower == ("milk", "eggs", "bread", "butter", "apples"):
    groceries == item_added.lower()
    groceries.remove(item_added)

print(groceries)

