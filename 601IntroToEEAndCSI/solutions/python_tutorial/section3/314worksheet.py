import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '../modules/'))

import checkers

def clip(lo, x, hi):
  if x < lo:
    return lo
  elif x > hi:
    return hi
  else:
    return x

question = clip(2, 1, 3)
checkers.check_answer(question, 2)

question = clip(3, 7, 9)
checkers.check_answer(question, 7)

question = clip(3, 12, 9)
checkers.check_answer(question, 9)
