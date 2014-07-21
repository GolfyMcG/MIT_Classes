import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '../modules/'))

import checkers
from math import pi
n = 0

def piSeries(n):
  seriesTotal = 4*sum([((-1.0)**i)/(2*i+1) for i in range(n)])
  return round(seriesTotal, 4)

def within(x, y, eps):
  return True if abs(x-y) < eps else False

def numTerms(eps):
  i = 1
  guess = 0
  check = pi
  while not within(guess, check, eps):
    guess = piSeries(i)
    i += 1
  return i, guess

n += 1
question = within(3, 4, 2)
ansvalue = True
checkers.check_answer(question, ansvalue, n)

n += 1
question = within(3, 5, 2)
ansvalue = False
checkers.check_answer(question, ansvalue, n)

n += 1
question = within(13, 4, 2)
ansvalue = False
checkers.check_answer(question, ansvalue, n)

print numTerms(0.1)
print numTerms(0.01)
print numTerms(0.001)
print numTerms(0.0001)
