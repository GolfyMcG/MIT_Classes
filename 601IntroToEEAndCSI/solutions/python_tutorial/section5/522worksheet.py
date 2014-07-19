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

def perpDist(p, l):
  (px, py) = p
  (a, b, c) = l

  cn = py - px*(b/a)
  xs = (-(c*a)/(b**2) - cn*(a/b))/(1 + ((a/b)**2))
  yo = (-a/b)*xs - (c/b)

  ps = (xs, yo)
  shrt_distance = round(pointDist(ps, p)*100)/100
  return shrt_distance

p = (10, 0)
l = (1, 1, 1)
question = perpDist(p, l)
checkers.check_answer(question, 7.81)
