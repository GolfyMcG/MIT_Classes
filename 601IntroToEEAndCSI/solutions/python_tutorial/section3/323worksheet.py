import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '../modules/'))

import checkers

def mod(m, n):
  if (isinstance(n, int) and n > 0) and (isinstance(m, int) and m > 0):
    while m > n:
      m = m - n

    return m
  else:
    print "Both arguments must be positive integers"


question = mod(3, 2)
checkers.check_answer(question, 1)

question = mod(2, 3)
checkers.check_answer(question, 2)

question = mod(11, 7)
checkers.check_answer(question, 4)

question = mod(11, 2)
checkers.check_answer(question, 1)
