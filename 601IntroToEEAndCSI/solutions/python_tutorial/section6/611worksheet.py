import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '../modules/'))

import checkers
n = 0

def zeroVector(n):
  return [0 for _ in range(n)]

n += 1
question = zeroVector(5)
ansvalue = [0, 0, 0, 0, 0]
checkers.check_answer(question, ansvalue, n)

n += 1
question = zeroVector(15)
ansvalue = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
checkers.check_answer(question, ansvalue, n)
