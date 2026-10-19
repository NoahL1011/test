"""
Filename: trivia_game.py
Author: <Laudat, Noah>
Created: <5/10/2026>
Instructor: Burgess
"""


score = 0
correct = 0


print ("welcome to trivia game")

y=input("What is the capitol city of australia?")
if y=="canberra":
    print("correct!!")
    score+=1
    correct+=1
else:
    print ("incorrect!!")
    if score > 0:
        score-=1

y=input("What is the chemical symbol for gold?")
if y=="au":
    print("correct!!")
    score+=1
    correct+=1
else:
    print ("incorrect!!")
    if score > 0:
        score-=1

y=input("In what year did the Berlin wall ofically fall?")
if y=="1989":
    print("correct!!")
    score+=1
    correct+=1
else:
    print ("incorrect!!")
    if score > 0:
        score-=1

y=input("Which acclaimed filmmaker directed Electric dreams 1984?")
if y=="Steve Barron":
    print("correct!!")
    score+=1
    correct+=1
else:
    print ("incorrect!!")
    if score > 0:
        score-=1

y=input("Which south american countries is completely landlocked?")
if y=="paraguay":
    print("correct!!")
    score+=1
    correct+=1
else:
    print ("incorrect!!")
    if score > 0:
        score-=1

y=input("Whats 1+1?")
if y=="2":
    print("correct!!")
    score+=1
    correct+=1
else:
    print ("incorrect!!")
    if score > 0:
        score-=1

y=input("When is Leif Erikson day?")
if y=="October 9th":
    print("correct!!")
    score+=1
    correct+=1
else:
    print ("incorrect!!")
    if score > 0:
        score-=1

y=input("When did my beloved amazing wonderous favorite band glass beach disband?")
if y=="April 30th 2026":
    print("correct!!")
    score+=1
    correct+=1
else:
    print ("incorrect!!")
    if score > 0:
        score-=1

y=input("What sad miserable art program does noah use to draw when he wishes he could just get krita, a drawing tablet"
        "his art diploma, and be DONE?")
if y=="Kleki":
    print("correct!!")
    score+=1
    correct+=1
else:
    print ("incorrect!!")
    if score > 0:
        score-=1

y=input("what is the best food out there?")
if y=="burek":
    print("correct!!")
    score+=1
    correct+=1
else:
    print ("incorrect!!")
    if score > 0:
        score-=1

print (f"your final score is {score}")
print (f"your total correct answers are {correct}/10")
print ("thank you for using this program i 100% wasnt forced to do for the sake of my GPA.")
