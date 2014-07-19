import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '../modules/'))

import checkers
import math

def multIA(m, n):
  product = 0

  for x in range(n):
    product = product + m

  return product

n = 1
question = multIA(3, 2)
ansvalue = 6
checkers.check_answer(question, ansvalue, n)

n += 1
question = multIA(3.5, 2)
ansvalue = 7
checkers.check_answer(question, ansvalue, n)
