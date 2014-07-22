import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '../modules/'))

import checkers
n = 0

def zeroVector(n):
  return [0 for _ in range(n)]

def zeroArray(m, n):
  return [zeroVector(n) for _ in range(m)]

v = zeroArray(3,4)
v[1][2] = 6

n += 1
question = v
ansvalue = [[0, 0, 0, 0], [0, 0, 6, 0], [0, 0, 0, 0]]
checkers.check_answer(question, ansvalue, n)
