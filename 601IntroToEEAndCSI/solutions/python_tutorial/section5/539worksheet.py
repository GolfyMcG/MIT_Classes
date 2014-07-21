import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '../modules/'))

import checkers
n = 0

def evalPolynomial(coeffs, x):
  n = len(coeffs)-1
  answer = sum([a*x**(n-i) for i,a in enumerate(coeffs)])

  return answer

n += 1
coeffs = [1, 2, 3]
x = 2
question = evalPolynomial(coeffs, x)
ansvalue = 11
checkers.check_answer(question, ansvalue, n)

n += 1
coeffs = [5, 3, 2, 1]
x = 4
question = evalPolynomial(coeffs, x)
ansvalue = 377
checkers.check_answer(question, ansvalue, n)
