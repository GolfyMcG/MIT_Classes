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

def multiAgen(m, n):
  if isinstance(n, int) and isinstance(m, int):
    if m < 0 and n < 0:
      a1 = abs(m)
      a2 = abs(n)
    elif m > 0 and n < 0:
      a1 = n
      a2 = m
    else:
      a1 = m
      a2 = n

    return multiA(a1, a2)
  else:
    print "Both arguments must be integers"


question = multiAgen(3, 2)
checkers.check_answer(question, 6)

question = multiAgen(-3, 2)
checkers.check_answer(question, -6)

question = multiAgen(-3, -2)
checkers.check_answer(question, 6)

question = multiAgen(3, -2)
checkers.check_answer(question, -6)
