import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '../modules/'))

import checkers

def mean(l):
  mean = float(sum(l))/len(l) if l else None
  return mean

n = 1
l = [1, 2, 3, 10]
question = mean(l)
ansvalue = 4
checkers.check_answer(question, ansvalue, n)

n += 1
l = [1, 2]
question = mean(l)
ansvalue = 1.5
checkers.check_answer(question, ansvalue, n)

n += 1
l = []
question = mean(l)
ansvalue = "None"
checkers.check_answer(question, ansvalue, n)
