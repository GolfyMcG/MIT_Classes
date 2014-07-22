import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '../modules/'))

import checkers
n = 0

def emptyAlist():
  return []

def addEntry(al, k, v):
  al.append([k, v])

def lookup(al, k):
  #return (pair for pair in al if pair[0] == k)
  for pair in al:
    if pair[0] == k:
      return pair

d = emptyAlist()
addEntry(d, 'key1', 'value1')
addEntry(d, 'key2', 'value2')

n += 1
question = d
ansvalue = [['key1', 'value1'], ['key2', 'value2']]
checkers.check_answer(question, ansvalue, n)

n += 1
question = lookup(d, 'key1')
ansvalue = ['key1', 'value1']
checkers.check_answer(question, ansvalue, n)

n += 1
question = lookup(d, 'key2')
ansvalue = ['key2', 'value2']
checkers.check_answer(question, ansvalue, n)
