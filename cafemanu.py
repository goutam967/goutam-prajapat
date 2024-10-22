#Define the menu of cafe
menu = {
     'pizza':120,
     'pasta':90,
     'cold coffee':80,
     'hot coffee':40,
     'burger':70,
     'noodles':100,
     'manchuriyan':110,
}

#Greet
print("welcome to PYTHON cafe")
print("pizza: Rs120\npasta: Rs90\ncold coffee: Rs80\nhot coffee: Rs40\nburger: Rs70\nnoodles: Rs100\nmanchuriyan: Rs110\n")

order_total=0
#120 + 110 = 230

item_1 = input("enter the name of item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"your item {item_1}has been added to your order")

else:
    print(f"orderd item {item_1}is not avaialable yet:")

another_order = input("do you want to add another item? (yes/no)")
if another_order == "yes":
    item_2 = input("enter the name off second item = ")
    if item_2 in menu:
        order_total += menu[item_2] #0 + 80
        print(f"item {item_2} has been added order ")
else:
        print(f"orderd item {item_2} is not avaialable!")

print(f"The total amount of item to pay is {order_total}")