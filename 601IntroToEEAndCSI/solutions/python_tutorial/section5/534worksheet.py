import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '../modules/'))

import checkers

def myRange(n):
  l = []
  i = 0
  while i < n:
    l.append(i)
    i += 1
  return l


n = 1
question = range(6)
ansvalue = myRange(6)
checkers.check_answer(question, ansvalue, n)

n += 1
question = range(9)
ansvalue = myRange(9)
checkers.check_answer(question, ansvalue, n)
