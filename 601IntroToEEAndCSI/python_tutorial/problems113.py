def check_answer(question, answer):
  if question == answer:
    print "Correct"
  else:
    print "Wrong"

check_answer(3 > 4, False)
check_answer(4.0 > 3.999, True)
check_answer(4 > 4, False)
check_answer(4 >= 4, True)
check_answer(2 + 2 == 4, True)
check_answer(True or False, True)
check_answer(False or False, False)
check_answer(not False, True)
check_answer(3.0 - 1.0 != 5.0 - 3.0, False)
check_answer(3 > 4 or (2 < 3 and 9 > 10), False)
check_answer(4 > 5 or 3 < 4 and 9 > 8, True)
check_answer(not(4 > 3 and 100 > 6), False)
