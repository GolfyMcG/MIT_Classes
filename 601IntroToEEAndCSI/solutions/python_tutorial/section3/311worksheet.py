import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '../modules/'))

import checkers
import math

def a(x, y, z):
  if x:
    return y
  else:
    return z

def b(y, z):
  return a(y>z, y, z)

question = a(False, 2, 3)
checkers.check_answer(question, 3)

question = b(3, 2)
checkers.check_answer(question, 3)

question = a(3>2, a, b)
checkers.check_answer(question, "Function")

question = b(a, b)
checkers.check_answer(question, "Function")
