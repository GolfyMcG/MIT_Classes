import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '../modules/'))

import checkers

n = 1
question = [0, 1, 2, 3, 4]
ansvalue = range(0, 5)
checkers.check_answer(question, ansvalue, n)

n += 1
question = [44, 45, 46]
ansvalue = range(44, 47)
checkers.check_answer(question, ansvalue, n)

n += 1
question = [-3, -2, -1, 0, 1]
ansvalue = range(-3, 2)
checkers.check_answer(question, ansvalue, n)

n += 1
question = [1, 3, 5, 7]
ansvalue = range(1, 8, 2)
checkers.check_answer(question, ansvalue, n)

n += 1
question = [5, 4, 3, 2]
ansvalue = range(5, 1, -1)
checkers.check_answer(question, ansvalue, n)
