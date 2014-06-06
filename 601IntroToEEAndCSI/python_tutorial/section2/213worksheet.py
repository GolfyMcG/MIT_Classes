import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '../modules/'))

import math
import checkers

def foo(x):
  def bar(x):
    return x + 1
  return bar(x*2)

question = foo(3)
checkers.check_answer(question, 7)
checkers.check_answer(type(question), int)

def foo(x):
  def bar(z):
    return z + x
  return bar(3)

question = foo(2)
checkers.check_answer(question, 5)
checkers.check_answer(type(question), int)
