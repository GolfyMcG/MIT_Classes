import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '../modules/'))

import checkers

def everyOther(l):
  return [l[x] for x in range(0, len(l), 2)]

n = 1
question = everyOther([1, 2, 3, 4, 5])
ansvalue = [1, 3, 5]
checkers.check_answer(question, ansvalue, n)

n += 1
question = everyOther(['this', 'is', 'a', 'sentence'])
ansvalue = ['this', 'a']
checkers.check_answer(question, ansvalue, n)

n += 1
question = everyOther(['oh no', 'this', 'is', 'a', 'another', 'longer', 'sentence'])
ansvalue = ['oh no', 'is', 'another', 'sentence']
checkers.check_answer(question, ansvalue, n)
