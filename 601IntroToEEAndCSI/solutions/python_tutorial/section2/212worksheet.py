import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '../modules/'))

import math
import checkers

a = 10
def f(x):
  return x + a
a = 3
question = f(1)
checkers.check_answer(question, 4)
checkers.check_answer(type(question), int)

x = 12
def g(x):
  x = x + 1
  def h(y):
    return x + y
  return h(6)

question = g(x)
checkers.check_answer(question, 19)
checkers.check_answer(type(question), int)
