import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '../modules/'))

import checkers
import math

def quadraticRootsComplex(a, b, c):
  a = float(a)
  b = float(b)
  c = float(c)

  if a == 0:
    return round((-c/b)*10)/10
  else:
    root = b**2-4*a*c
    if root < 0:
      root = abs(root)
      j = complex(0,1)
      x1 = (-b + j * math.sqrt(root))/(2*a)
      x2 = (-b - j * math.sqrt(root))/(2*a)
      return [x1, x2]
    else:
      x1 = (-b + math.sqrt(root))/(2*a)
      x2 = (-b - math.sqrt(root))/(2*a)
      return sorted([x1, x2])

question = quadraticRootsComplex(1, 2, -3)
checkers.check_answer(question, sorted([-3, 1]))

question = quadraticRootsComplex(1, 2, -3)
checkers.check_answer(question, sorted([1, -3]))

question = quadraticRootsComplex(0, 2, -3)
checkers.check_answer(question, 1.5)

question = quadraticRootsComplex(1, -2, 5)
checkers.check_answer(question, [complex(1,+2), complex(1,-2)])
