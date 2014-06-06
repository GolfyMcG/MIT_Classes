import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '../modules/'))

import checkers

#This is just asking for me to create a function that checks if something is odd!

def odd(x):
  return not (x % 2 == 0)

question = odd(128982)
checkers.check_answer(question, False)

question = odd(37)
checkers.check_answer(question, True)
