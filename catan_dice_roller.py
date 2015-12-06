# -*- coding:utf-8 -*-
from random import randint
from sys import exit



def roll():
    a = randint(1, 6)
    b = randint(1, 6)
    
    write = raw_input("Press enter to roll >>>>>")

    if write == "":
        print "Dice A = ", a
        print "Dice B = ", b
        print "Sum is >>>>>>>>> ", a + b ," <<<<<<<<<"

    
    elif write == "quit":
        exit(0)

    else:
        print "Press ENTER BUTTON please！"
        
    roll()
    
roll()
