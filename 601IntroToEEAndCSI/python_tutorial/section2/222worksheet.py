import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '../modules/'))

import checkers

#This is just asking for me to create a function that squares things!

def square(x):
  return x**2

def fourthPower(x):
  return square(square(x))

question = fourthPower(2)
checkers.check_answer(question, 16)

question = fourthPower(3)
checkers.check_answer(question, 81)
