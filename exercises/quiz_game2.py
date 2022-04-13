print("Welcome to my computer quiz!")

playing = input ("Would you like to play my game? ").lower()
if playing != "yes".lower():
    quit()

score = 0

answer = input("What is the meaning of CPU? ").lower()
if answer == "central processing unit".lower():
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What is the meaning of GPU? ").lower()
if answer == "graphics processing unit".lower():
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What is the meaning of RAM? ").lower()
if answer == "random access memory".lower():
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What is the meaning of PSU? ").lower()
if answer == "power supply unit".lower():
    print("Correct!")
    score += 1
else:
    print("Incorrect")

print("You got " + str(score) + " correct")

print("You got " + str((score / 4) * 100) + "%")