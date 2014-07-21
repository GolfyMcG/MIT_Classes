import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '../modules/'))

import checkers
n = 0

def zeroVector(n):
  return [0 for _ in range(n)]

def zeroArray(m, n):
  baseVector = zeroVector(n)
  return [baseVector for _ in range(m)]

n += 1
question = zeroArray(3, 3)
ansvalue = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
checkers.check_answer(question, ansvalue, n)

n += 1
question = zeroArray(4, 3)
ansvalue = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
checkers.check_answer(question, ansvalue, n)

n += 1
question = zeroArray(3, 4)
ansvalue = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
checkers.check_answer(question, ansvalue, n)
