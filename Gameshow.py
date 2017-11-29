# John Heitz
# 11/28/2017
# Game Show
import random
play_again="Yes"
print ("Welcome to the games.You have to open a door and get your loot")
while play_again=="Yes":
    prize=random.randint(1,4)
    if prize==1:
        prize=("You got a burrito")
    if prize==2:
        prize=("You got a tuna flavored book")
    if prize==3:
        prize=("You got nothing")
    if prize==4:
        prize=("You got hypnotised")
    door=input("Do you choose door 1, door 2, door 5. Sorry It was 3, or door 4.")
    if door=="door 1":    
       print(prize)
       play_again=input("Do you want to play again(Please put Yes or No): ")
    elif door=="door 2":
       print(prize)
       play_again=input("Do you want to play again(Please put Yes or No): ")
    elif door=="door 3":
       print(prize)
       play_again=input("Do you want to play again(Please put Yes or No): ") 
    elif door=="door 4":
       print(prize)
       play_again=input("Do you want to play again(Please put Yes or No): ") 
    elif door=="door 5":
        print ("How did you find out about seceret door 5 and now monty python will kill me")
        play_again=input("Do you want to play again(Please put Yes or No): ")
    else:
        print("Bad boy")
        play_again=input("Do you want to play again(Please put Yes or No): ")
