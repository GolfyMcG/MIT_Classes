import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '../modules/'))

import checkers

#This is just asking for me to create a function that squares things!

def square(x):
  return x**2

question = square(2)
checkers.check_answer(question, 4)

question = square(9)
checkers.check_answer(question, 81)
