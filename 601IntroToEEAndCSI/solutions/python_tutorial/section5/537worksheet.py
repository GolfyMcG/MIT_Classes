import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '../modules/'))

import checkers

x = {}
x['a']='apple'
x['b']='banana'
x['c']='chili dog'

n = 1
question = x['c']
ansvalue = 'chili dog'
checkers.check_answer(question, ansvalue, n)

# n += 1
# question = x['banana']
# ansvalue = "Error"
# checkers.check_answer(question, ansvalue, n)

n += 1
x['a']=37
question = x['a']
ansvalue = 37
checkers.check_answer(question, ansvalue, n)

n += 1
question = x.has_key('a')
ansvalue = True
checkers.check_answer(question, ansvalue, n)
