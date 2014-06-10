import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '../modules/'))

import checkers

def compare(x,y):
  if x > y:
    return 1
  elif x == y:
    return 0
  else:
    return -1

question = compare(1,1)
checkers.check_answer(question, 0)

question = compare(2,7)
checkers.check_answer(question, -1)

question = compare(8,5)
checkers.check_answer(question, 1)
