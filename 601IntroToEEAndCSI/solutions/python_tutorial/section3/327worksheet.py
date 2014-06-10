import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '../modules/'))

import checkers

def perfectSquare(n):
  if isinstance(n, int) and n > 0:
    i = 1
    test = 0
    ans = False

    while test < n:
      test = i*i
      if n == test:
        ans = True
      i = i + 1

    return ans
  else:
    print "Argument must be a positive integer"


question = perfectSquare(9)
checkers.check_answer(question, True)

question = perfectSquare(8)
checkers.check_answer(question, False)

question = perfectSquare(625)
checkers.check_answer(question, True)

question = perfectSquare(62)
checkers.check_answer(question, False)
