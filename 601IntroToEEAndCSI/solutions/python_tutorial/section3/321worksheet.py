import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '../modules/'))

import checkers

def multiA(m, n):
  if n > 0 and isinstance(n, int):
    i = 1
    total = 0
    while i <= n:
      total = total + m
      i = i + 1

    return round(total*10) / 10
  else:
    print "The second argument must be a positive integer"

question = multiA(1, 2)
checkers.check_answer(question, 2)

question = multiA(3.2, 3)
checkers.check_answer(question, 9.6)

question = multiA(7.7, 3)
checkers.check_answer(question, 23.1)
