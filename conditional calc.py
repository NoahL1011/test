"""
Filename: conditonal calc.py
Author: <Laudat, Noah>
Created: <5/10/2026>
Instructor: Burgess
"""






print("Welcome to the simple calculator")

num1 = int(input("Enter a number"))
op = input("what is your operation: ")
num2 = int(input("Enter a second number: "))
print(num1 + num2)
if op=="+":
    print(f"{num1} + {num2} = {num1 + num2}")
elif op=="-":
    print(f"{num1} - {num2} = {num1 - num2}")
elif op=="*":
    print(f"{num1} * {num2} = {num1 * num2}")
elif op=="/":
    print(f"{num1} / {num2} = {num1 / num2}")


print("thank you for using this program")
