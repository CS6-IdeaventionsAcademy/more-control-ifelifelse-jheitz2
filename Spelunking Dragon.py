# John Heitz
# 11/29/2017
# Spelunking Dragon
dragon=input("You are a dragon in a cave. Which speices of dragon are you (Fire, Air, Water, Earth, Plant, or Shadow): ")
if dragon=="Fire":
    natural_weapon="fire breath"
    explosion="blows up"
if dragon=="Air":
    natural_weapon="fire breath"
    explosion="blows up"
if dragon=="Earth":
    natural_weapon="fire breath"
    explosion="blows up"
if dragon=="Shadow":
    natural_weapon="fire breath"
    explosion="blows up"
if dragon=="Ice":
    natural_weapon="ice breath"
    explosion="blows up"
if dragon=="Plant":
    natural_weapon="venom"
    explosion="melts"
coice1=input ("You got caved in and your dragon kind cannot see or hear you for miles. There is a fork in the cave do you want to go left or right: ")
if coice1=="left":
    choice2=input("A boulder is blocking your path. Do you want to use your " +natural_weapon+" on it(use caps on the first letter).")
    if choice2=="Yes":
        choice3=input ("The bolder "+explosion + " and you find a dead end. Do you want to turn around or explore it: ")
        if choice3=="shoot the roof":
            print("You fly out and go back to your dragon kingdom. You win.")
        else:
            print("The cave caves in and you die")
    if choice2=="No":
        print("The cave caves in and you suffocate")
##if choice1==("right")
##            choice2=input("You see a tap dancing pug, do you want to kill it or dance with it: ")
##            if choice2=="eat it":
##                print("King Levi flies down and kills you for killing his brother.")
##            else:
##                print("It eats you")
