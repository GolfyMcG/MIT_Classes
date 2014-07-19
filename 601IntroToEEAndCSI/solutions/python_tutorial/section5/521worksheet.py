import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '../modules/'))

import checkers
import math

def pointDist(p1, p2):
  dx = p1[0] - p2[0]
  dy = p1[1] - p2[1]
  result = round(math.sqrt(dx**2 + dy**2), 3)
  return result

p1 = (0, 4)
p2 = (3, 0)

n = 1
question = pointDist(p1, p2)
ansvalue = 5
checkers.check_answer(question, ansvalue, n)

p1 = (2, 4)
p2 = (3, 7)

n += 1
question = pointDist(p1, p2)
ansvalue = 3.162
checkers.check_answer(question, ansvalue, n)

p1 = (5, 4)
p2 = (3, 13)

n += 1
question = pointDist(p1, p2)
ansvalue = 9.220
checkers.check_answer(question, ansvalue, n)
