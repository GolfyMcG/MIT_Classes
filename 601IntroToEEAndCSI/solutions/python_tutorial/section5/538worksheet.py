import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '../modules/'))

import checkers
n = 0

def piSeries(n):
  seriesTotal = 4*sum([((-1.0)**i)/(2*i+1) for i in range(n)])
  return round(seriesTotal, 4)

n += 1
question = piSeries(10000)
ansvalue = 3.1415
checkers.check_answer(question, ansvalue, n)

n += 1
question = piSeries(100000)
ansvalue = 3.1416
checkers.check_answer(question, ansvalue, n)
