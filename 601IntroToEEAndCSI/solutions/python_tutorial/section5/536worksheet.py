import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '../modules/'))

import checkers
from math import sqrt

def mean(l):
  mean = float(sum(l))/len(l) if l else None
  return mean

def stddev(l):
  n = float(len(l))
  if n > 2:
    meanVariation = 0
    for x in l:
      meanVariation += (x - mean(l))**2
    stddev = sqrt((1/(n-1))*meanVariation)
  else:
    stddev = 0.0

  return round(stddev, 2)

n = 1
l = [1, 2, 3, 10]
question = stddev(l)
ansvalue = 4.08
checkers.check_answer(question, ansvalue, n)

n += 1
l = [1, 2]
question = stddev(l)
ansvalue = 0.0
checkers.check_answer(question, ansvalue, n)

n += 1
l = []
question = stddev(l)
ansvalue = 0.0
checkers.check_answer(question, ansvalue, n)

n = 1
l = [141, 21, 3, 10]
question = stddev(l)
ansvalue = 65.26
checkers.check_answer(question, ansvalue, n)
