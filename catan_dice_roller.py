# -*- coding:utf-8 -*-
from random import randint

def roll():
    a = randint(1, 6)
    b = randint(1, 6)
  
  write = raw_input("Press enter to roll >>>>>")

  if write == "":
		print a + b
		roll()
	else:
		print "Press ENTER BUTTON please！"
		roll()

roll()
