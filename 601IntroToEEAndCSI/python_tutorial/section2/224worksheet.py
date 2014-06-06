import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '../modules/'))

import checkers
import math

#This is just asking for me to create a function that calculates distance!

def pointDist(x1, y1, x2, y2):
  d1 = x2 - x1
  d2 = y2 - y1
  square_distance = d1**2 + d2**2
  distance = math.sqrt(square_distance)
  return distance

question = pointDist(0, 1, 3, 1)
checkers.check_answer(question, 3)

question = pointDist(4, 1, 4, 1)
checkers.check_answer(question, 0)

question = pointDist(4, 1, 4, 7)
checkers.check_answer(question, 6)

question = pointDist(0, 0, 4, 3)
checkers.check_answer(question, 5)
