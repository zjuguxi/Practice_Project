# -*- coding:utf-8 -*-
from random import randint
from sys import exit

print '''
Hello, stranger!
It is time to come to the world of Dungeons&Drangons.
ROLL to face to your fate!

HOHOHOHOHO~~~~
'''

def choose():
    print '''What do you want?
    A---2d6
    B---2d10
    C---3d4
    '''
    input = raw_input(">  ")

    if input == "A":
        roll_2d6()
    elif input == "B":
        roll_2d10()
    elif input == "C":
        roll_3d4()
    else:
        print "Make your choise!"
    
    choose()

def roll_2d6():
    a = randint(1, 6)
    b = randint(1, 6)
    
    write = raw_input("Press enter to roll 2D6 ('q' to quit, '2d10', '3d4')>>>>>")

    if write == "":
        print "Dice A = ", a
        print "Dice B = ", b
        print "Sum is >>>>>>>>> ", a + b ," <<<<<<<<<"

    
    elif write == "q":
        exit(0)
    elif write == "2d10":
        roll_2d10()

    else:
        print "Press ENTER BUTTON please！"
    
    roll_2d6()
    
def roll_2d10():
    a = randint(1, 10)
    b = randint(1, 10)
    
    write = raw_input("Press enter to roll 2D10 ('q' to quit, '2d6', '3d4')>>>>>")

    if write == "":
        print "Dice A = ", a
        print "Dice B = ", b
        print "Sum is >>>>>>>>> ", a + b ," <<<<<<<<<"

    
    elif write == "q":
        exit(0)

    elif write == "2d6":
        roll_2d6()
    elif write == "3d4":
        roll_3d4()

    else:
        print "Press ENTER BUTTON please！"
    
    roll_2d10()

def roll_3d4():
    a = randint(1, 4)
    b = randint(1, 4)
    c = randint(1, 4)
    
    write = raw_input("Press enter to roll 3D4 ('q' to quit, '2d6', '2d10')>>>>>")

    if write == "":
        print "Dice A = ", a
        print "Dice B = ", b
        print "Dice C = ", c
        print "Sum is >>>>>>>>> ", a + b + c," <<<<<<<<<"

    
    elif write == "q":
        exit(0)

    elif write == "2d6":
        roll_2d6()
    elif write == "2d10":
        roll_2d10()

    else:
        print "Press ENTER BUTTON please！"
    
    roll_3d4()

choose()
