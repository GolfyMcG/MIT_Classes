import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '../modules/'))

import checkers

def cat6(l):
  n = l + [6]
  return n

n = 1
question = cat6([1, 2, 3, 4, 5])
ansvalue = [1, 2, 3, 4, 5, 6]
checkers.check_answer(question, ansvalue, n)

n += 1
question = cat6(['this', 'is', 'a', 'sentence'])
ansvalue = ['this', 'is', 'a', 'sentence', 6]
checkers.check_answer(question, ansvalue, n)
