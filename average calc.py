"""
Filename: average calc.py
Author: <Laudat, Noah>
Created: <27/10/2026>
Instructor: Burgess
"""

total = 0
amount = 0
print("welcome to the average calculator")

reply="y"
while reply == "y":


    num = int(input("Enter a number"))
    total+=num
    amount+=1

    print (f"total:{total}")
    print(f"amount:{amount}")
    print(f"average:{total/amount}")

    reply=input("do you want to enter another number? y/n:")
