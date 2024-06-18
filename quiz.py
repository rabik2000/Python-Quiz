print("Welcome to Football Quiz")

playing = input("Do you want to play (y/n)? :  ")

if playing.lower() != "y":
    quit()

print("Okay, Let's play \n")
score = 0

answer = input("Who won the first football world cup? ")
if answer.lower() == "uruguay":
    print('Correct \n')
    score += 1
else:
    print('Incorrect \n')

answer = input("Who is the all time top-scorer in football world cup history? ")
if answer.lower() == "klose":
    print('Correct \n')
    score += 1
else:
    print('Incorrect \n')

answer = input("How many UCl has Cristiano Ronaldo won? ")
if answer.lower() == "5":
    print('Correct \n')
    score += 1
else:
    print('Incorrect \n')

answer = input("How many UCl has Manchester United won? ")
if answer.lower() == "3":
    print('Correct \n')
    score += 1
else:
    print('Incorrect \n')

answer = input("How won the 2012 EURO CUP? ")
if answer.lower() == "italy":
    print('Correct \n')
    score += 1
else:
    print('Incorrect \n')

print("You got " + str(score) + " questions correct \n")
print("You got " + str((score / 5) * 100) + " % \n")