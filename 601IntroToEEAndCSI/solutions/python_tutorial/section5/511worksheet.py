import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '../modules/'))

import checkers

a = 'hi'
x = [1, 2, [3, 'John', 4], 'Hi']

n = 1
question = a
ansValue = 'hi'
ansType = str
checkers.check_answer(question, ansValue, n)
checkers.check_answer(type(question), ansType, n)

n = 2
question = a[0]
ansValue = 'h'
ansType = str
checkers.check_answer(question, ansValue, n)
checkers.check_answer(type(question), ansType, n)

n = 3
question = a[1]
ansValue = 'i'
ansType = str
checkers.check_answer(question, ansValue, n)
checkers.check_answer(type(question), ansType, n)

n = 4
# question = a[2]
# ansValue = "Error"
# ansType = "Error"
# checkers.check_answer(question, ansValue, n)
# checkers.check_answer(type(question), ansType, n)

n = 5
question = x[0]
ansValue = 1
ansType = int
checkers.check_answer(question, ansValue, n)
checkers.check_answer(type(question), ansType, n)

n = 6
question = x[2]
ansValue = [3, 'John', 4]
ansType = list
checkers.check_answer(question, ansValue, n)
checkers.check_answer(type(question), ansType, n)

n = 7
question = x[-1]
ansValue = 'Hi'
ansType = str
checkers.check_answer(question, ansValue, n)
checkers.check_answer(type(question), ansType, n)

n = 8
question = x[2][2]
ansValue = 4
ansType = int
checkers.check_answer(question, ansValue, n)
checkers.check_answer(type(question), ansType, n)

n = 9
question = x[2][-1]
ansValue = 4
ansType = int
checkers.check_answer(question, ansValue, n)
checkers.check_answer(type(question), ansType, n)

n = 10
# question = x[-1][2]
# ansValue = "Error"
# ansType = "Error"
# checkers.check_answer(question, ansValue, n)
# checkers.check_answer(type(question), ansType, n)

n = 11
question = x[0:1]
ansValue = [1]
ansType = list
checkers.check_answer(question, ansValue, n)
checkers.check_answer(type(question), ansType, n)

n = 12
question = x[0:-1]
ansValue = [1, 2, [3, 'John', 4]]
ansType = list
checkers.check_answer(question, ansValue, n)
checkers.check_answer(type(question), ansType, n)

n = 13
question = len(x)
ansValue = 4
ansType = int
checkers.check_answer(question, ansValue, n)
checkers.check_answer(type(question), ansType, n)

(a, b, c, d) = x
n = 14
question = c
ansValue = [3, 'John', 4]
ansType = list
checkers.check_answer(question, ansValue, n)
checkers.check_answer(type(question), ansType, n)

n = 15
question = range(3)
ansValue = [0, 1, 2]
ansType = list
checkers.check_answer(question, ansValue, n)
checkers.check_answer(type(question), ansType, n)

n = 16
question = range(3, 10)
ansValue = [3, 4, 5, 6, 7, 8, 9]
ansType = list
checkers.check_answer(question, ansValue, n)
checkers.check_answer(type(question), ansType, n)

n = 17
question = range(3, 10, 3)
ansValue = [3, 6, 9]
ansType = list
checkers.check_answer(question, ansValue, n)
checkers.check_answer(type(question), ansType, n)

n = 18
question = range(10, 3)
ansValue = []
ansType = list
checkers.check_answer(question, ansValue, n)
checkers.check_answer(type(question), ansType, n)

n = 19
question = range(10, 3, -1)
ansValue = [10, 9, 8, 7, 6, 5, 4]
ansType = list
checkers.check_answer(question, ansValue, n)
checkers.check_answer(type(question), ansType, n)

n = 20
question = range(len(x))
ansValue = [0, 1, 2, 3]
ansType = list
checkers.check_answer(question, ansValue, n)
checkers.check_answer(type(question), ansType, n)

n = 21
question = 'hi' == 'Hi'
ansValue = False
ansType = bool
checkers.check_answer(question, ansValue, n)
checkers.check_answer(type(question), ansType, n)

n = 22
question = 2 in x
ansValue = True
ansType = bool
checkers.check_answer(question, ansValue, n)
checkers.check_answer(type(question), ansType, n)

n = 23
question = 3 in x
ansValue = False
ansType = bool
checkers.check_answer(question, ansValue, n)
checkers.check_answer(type(question), ansType, n)

n = 24
question = 'John' in x
ansValue = False
ansType = bool
checkers.check_answer(question, ansValue, n)
checkers.check_answer(type(question), ansType, n)

n = 25
question = 'Hi' in x
ansValue = True
ansType = bool
checkers.check_answer(question, ansValue, n)
checkers.check_answer(type(question), ansType, n)

n = 26
question = sum(range(4))
ansValue = 6
ansType = int
checkers.check_answer(question, ansValue, n)
checkers.check_answer(type(question), ansType, n)

n = 27
question = [x for x in range(3)]
ansValue = [0, 1, 2]
ansType = list
checkers.check_answer(question, ansValue, n)
checkers.check_answer(type(question), ansType, n)

n = 28
question = [x*2 for x in range(3)]
ansValue = [0, 2, 4]
ansType = list
checkers.check_answer(question, ansValue, n)
checkers.check_answer(type(question), ansType, n)

n = 29
question = sum([x*2 for x in range(3)])
ansValue = 6
ansType = int
checkers.check_answer(question, ansValue, n)
checkers.check_answer(type(question), ansType, n)

n = 30
question = [-x for x in [8, 2, 1] ]
ansValue = [-8, -2, -1]
ansType = list
checkers.check_answer(question, ansValue, n)
checkers.check_answer(type(question), ansType, n)

def fizz(x):
  return x + 1

n = 31
question = [fizz(fizz(x)) for x in [8, 2, 1]]
ansValue = [10, 4, 3]
ansType = list
checkers.check_answer(question, ansValue, n)
checkers.check_answer(type(question), ansType, n)

n = 32
question = [x for x in range(10) if x%2 == 0]
ansValue = [0, 2, 4, 6, 8]
ansType = list
checkers.check_answer(question, ansValue, n)
checkers.check_answer(type(question), ansType, n)
