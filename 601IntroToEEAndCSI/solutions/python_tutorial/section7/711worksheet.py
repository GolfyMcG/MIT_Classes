import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '../modules/'))

import checkers
n = 0

def emptyAlist():
  return []

def addEntry(al, k, v):
  al.append([k, v])

d = emptyAlist()
addEntry(d, 'key1', 'value1')

n += 1
question = d
ansvalue = [['key1', 'value1']]
checkers.check_answer(question, ansvalue, n)

addEntry(d, 'key2', 'value2')

n += 1
question = d
ansvalue = [['key1', 'value1'], ['key2', 'value2']]
checkers.check_answer(question, ansvalue, n)
