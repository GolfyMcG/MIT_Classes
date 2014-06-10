import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '../modules/'))

import checkers

def arithmetic(v, a, b, c):
  if v > 0:
    return a
  elif v == 0:
    return b
  else:
    return c

question = arithmetic(1, 2, 3, 4)
checkers.check_answer(question, 2)

question = arithmetic(0, 2, 3, 4)
checkers.check_answer(question, 3)

question = arithmetic(-2, 2, 3, 4)
checkers.check_answer(question, 4)

question = arithmetic(-2, "blah", "bleh", "nom")
checkers.check_answer(question, "nom")
