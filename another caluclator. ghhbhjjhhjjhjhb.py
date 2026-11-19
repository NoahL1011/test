"""
Filename: factoral calc.py
Author: <Laudat, Noah>
Created: <27/10/2026>
Instructor: Burgess
"""



def factorial():
    # Write your code here
    total = 1
    num = int(input("Enter a number"))
    if num == 0:
        print("0!=1")
    else:
        print(f"{num}!=",end="")
        for p in range(num,0,-1):
            if p > 1:
                print(f"{p}*", end="")
            else:
                print(f"{p}", end="")
            total *= p
        print("=",total)



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
