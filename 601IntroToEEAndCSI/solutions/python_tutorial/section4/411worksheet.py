import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '../modules/'))

import checkers
import math

def quadraticRoots(a, b, c):
  a = float(a)
  b = float(b)
  c = float(c)

  if a == 0:
    return round((-c/b)*10)/10
  else:
    x1 = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
    x2 = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)
    return sorted([x1, x2])

question = quadraticRoots(1, 2, -3)
checkers.check_answer(question, sorted([-3, 1]))

question = quadraticRoots(1, 2, -3)
checkers.check_answer(question, sorted([1, -3]))

question = quadraticRoots(0, 2, -3)
checkers.check_answer(question, 1.5)
