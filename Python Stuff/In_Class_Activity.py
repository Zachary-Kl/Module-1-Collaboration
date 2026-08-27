# Author: Zachary Klopp
# File Name: In_Class_Activity.py
# Description: Product price calculator that includes a discount when above a set price.

while True:
    product_name = input("Please input whether you want a book, pen, bag or input ZZZ to stop: ")
    if product_name == "ZZZ":
        print("User inputted ZZZ so ending program.")
        break
    elif product_name == "book":
        price = 10.00   
    elif product_name == "pen":
        price = 2.00
    elif product_name == "bag":
        price = 5.00
    else:
        print("Invalid input please retry")
    if price >= 5.00:
        print("Discount applied")
    else:
        print("No discount applied")