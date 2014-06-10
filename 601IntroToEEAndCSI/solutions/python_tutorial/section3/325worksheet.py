import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '../modules/'))

import checkers

def prime(n):
  if n > 0 and isinstance(n, int):
    i = 2
    while i < n:
      if n%i == 0:
        prime = False
        break
      else:
        prime = True
      i = i + 1

    return prime
  else:
    print "Argument must be a positive integer"


question = prime(6)
checkers.check_answer(question, False)

question = prime(5)
checkers.check_answer(question, True)

question = prime(15)
checkers.check_answer(question, False)

question = prime(23)
checkers.check_answer(question, True)
