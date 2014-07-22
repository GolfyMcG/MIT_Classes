import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '../modules/'))

import checkers
n = 0

def sumArray1(a):
  return sum([sum(i) for i in a])

def flatten(l):
  out = []
  for item in l:
    if isinstance(item, (list, tuple)):
      out.extend(flatten(item))
    else:
      out.append(item)
  return out

def sumArray2(a):
  return sum(flatten(a))

n += 1
a = [[1, 2], [3, 4], [5, 6]]
question = sumArray1(a)
ansvalue = 21
checkers.check_answer(question, ansvalue, n)

n += 1
a = [[3, 12], [13, 4]]
question = sumArray1(a)
ansvalue = 32
checkers.check_answer(question, ansvalue, n)

n += 1
a = [[1, 2], [3, 4], [5, 6]]
question = sumArray2(a)
ansvalue = 21
checkers.check_answer(question, ansvalue, n)

n += 1
a = [[3, 12], [13, 4]]
question = sumArray2(a)
ansvalue = 32
checkers.check_answer(question, ansvalue, n)
