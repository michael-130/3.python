
print("Welcome to my Computer pyhton Project!")

playing = input("Do you wanna to play? ")


if playing != "yes":
    quit()

print("Okay! Lets play:)")
score=0
#1
answer = input("What dose CPU stand for? ")
if answer.lower() == "central processing unit":
   print("Correct!")
   score+=20
else:
    print("Incorrect!")

    
#2
answer = input("What dose GPU stand for? ")
if answer.lower()== "graphics processing unit":
   print("Correct!")
   score+=20
else:
    print("Incorrect!")

#3
answer = input("What dose RAM stand for? ")
if answer.lower()== "random access memory":
   print("Correct!")
   score+=20
else:
    print("Incorrect!")

#4
answer = input("What dose PSU stand for? ")
if answer.lower()== "power supply":
   print("Correct!")
   score+=20
else:
    print("Incorrect!")

#5
answer = input("What dose PC stand for? ")
if answer.lower()== "personal computer":
   print("Correct!")
   score+=20
else:
    print("Incorrect!")

# if score == 80 or score == 100:print("Well played,You Got " + str(score) +" Score!") else:print("Nice try ,You got " +  str(score) ) ini yang panjangnya
     
# ini pendeknya
if score >= 60 :
   print("Well played! You got  " + str(score) + "  Score!" ) 

else : 
    print("Nice try! You got " + str(score) + " Score!")

print("You got " + str((score / 5) * 100) + "%.")

# jangan kayak gini print("You got " + str((score / 5)) * 100 +"%.")