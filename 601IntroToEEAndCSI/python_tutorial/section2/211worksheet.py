import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '../modules/'))

import math
import checkers

def a(x):
  return x + 1

checkers.check_answer(type(a(1)), int)

def b(x):
  return x + 1.0
checkers.check_answer(type(b(1)), float)

def c(x, y):
  return x + y

#Answer is num
checkers.check_answer(type(c(1, 1)), int)
checkers.check_answer(type(c(1, 1.0)), float)
checkers.check_answer(type(c(1.0, 1.0)), float)

def d(x, y):
  return x > y

checkers.check_answer(type(d(1,2)), bool)

def e(x, y, z):
  return x >= y and x <= z

checkers.check_answer(type(e(1,2,3)), bool)

def f(x, y):
  x + y - 2

checkers.check_answer(type(f(1,2)), "NoneType")
