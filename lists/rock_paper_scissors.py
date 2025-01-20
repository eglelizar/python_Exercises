# rock > scissors > paper > rock
import random

options = ["rock", "scissors", "paper"]

print("Welcome to the game rock, scissors, paper!!!!!")
usersOption = int(input ("What is your option? 0:Rock, 1:Scissors, 2:Paper: "))
computersOption = random.randint(0,2)


print ("Computer's option was: " + options[computersOption])

if (computersOption == usersOption):
    print ("Draw, tie!!!! Both won/lose!")
#User has a rock
elif (usersOption == 0):
        #Computer has a scissor
        if (computersOption == 1):
            print ("You won!!!!")
        else:
            print ("You lose!!!")
#User has scissors
elif(usersOption == 1):
     #Computer has a rock
    if (computersOption ==0):
          print ("You lose!!!")
    #Computer has a paper
    else:
         print ("You won!!")
#User has a paper
elif (usersOption ==2):
        #Computer has a rock
    if (computersOption ==1):
        print("You lose!!!")
    else:
        print("You win!!")
else:
     print ("Please input a valid option!!!!")



    
