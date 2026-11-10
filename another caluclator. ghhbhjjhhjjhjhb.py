"""
Filename: factoral calc.py
Author: <Laudat, Noah>
Created: <27/10/2026>
Instructor: Burgess
"""



def factorial():
    # Write your code here


# You should not need to change any code below this point
def main():
    print("This program computes factorials and displays their intermediate calculations.")
    running = "y"
    while running == "y":
        factorial()
        running = input("Do another calculation? (y/N)\n").lower()
    print("Thank you for using this factorial calculator!")

if __name__ == "__main__":
    main()