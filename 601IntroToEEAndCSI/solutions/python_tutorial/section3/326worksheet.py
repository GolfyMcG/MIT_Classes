import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '../modules/'))

import checkers

def p2(x):
  if isinstance(x, int):
    if x > 1:
      i = 1
      while i < x:
        ans = i
        i = i*2

      return ans
    else:
      return 0
  else:
    print "Argument must be an integer"


question = p2(9)
checkers.check_answer(question, 8)

question = p2(-1)
checkers.check_answer(question, 0)

question = p2(3)
checkers.check_answer(question, 2)

question = p2(17)
checkers.check_answer(question, 16)

question = p2(16)
checkers.check_answer(question, 8)
