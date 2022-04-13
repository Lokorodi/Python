print("Welcome to my computer quiz!")

playing = input("Do you want to play? ").lower()

if playing != "yes".lower():
    quit()

print("Okay, Let's play!")
score = 0

answer = input ("What is the meaning of CPU? ").lower()
if answer == "central processing unit".lower():
    print("Correct")
    score += 1
else:
    print("Incorrect")
    

answer = input ("What is the meaning of GPU? ").lower()
if answer == "graphics processing unit".lower():
    print("Correct")
    score += 1
else:
    print("Incorrect")
    


answer = input ("What is the meaning of PSU? ").lower()
if answer == "power supply unit".lower():
    print("Correct")
    score += 1 
else:
    print("Incorrect")
       


answer = input ("What is the meaning of RAM? ").lower()
if answer == "random access memory".lower():
    print("Correct")
    score += 1
else:
    print("Incorrect")
    

print("you got " + str(score) + " correct!")