import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '../modules/'))

import checkers
import math

#This is just asking for me to create a function that calculates the value of a quadratic equation!

def evalQuadratic(a, b, c, x):
  return a*x**2 + b*x + c

question = evalQuadratic(1, 1, 1, 1)
checkers.check_answer(question, 3)

question = evalQuadratic(2, 2, 2, 2)
checkers.check_answer(question, 14)

question = evalQuadratic(2, 3, 4, 5)
checkers.check_answer(question, 69) #hehe
