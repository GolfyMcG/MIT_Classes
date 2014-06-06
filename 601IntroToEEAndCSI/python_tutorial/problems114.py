import math

def check_answer(question, answer):
  if question == answer:
    print "Correct"
  else:
    print "Wrong"

check_answer(type(3 + 5.0), float)
check_answer(type(5/2), int)
check_answer(type(5/2 == 5/2.0), bool)
check_answer(type(5/2.0), float)
check_answer(type(round(2.6)), float)
check_answer(type(int(2.6)), int)
check_answer(type(math.floor(2.6)), float)
check_answer(type(2.0 + 5.0), float)
check_answer(type( 5 * 2 == 5.0 * 2.0), bool)
