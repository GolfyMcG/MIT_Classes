import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '../modules/'))

import checkers

def div(m, n):
  if (isinstance(n, int) and n > 0) and (isinstance(m, int) and m > 0):
    i = 0
    while m >= n:
      m = m - n
      i = i + 1

    return i
  else:
    print "Both arguments must be positive integers"


question = div(3, 2)
checkers.check_answer(question, 1)

question = div(2, 3)
checkers.check_answer(question, 0)

question = div(11, 7)
checkers.check_answer(question, 1)

question = div(11, 2)
checkers.check_answer(question, 5)

question = div(6, 2)
checkers.check_answer(question, 3)
