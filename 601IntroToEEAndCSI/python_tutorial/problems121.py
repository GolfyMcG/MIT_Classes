def check_answer(question, answer):
  if question == answer:
    print "Correct"
  else:
    print "Wrong"

a = 3
check_answer(a + 2.0, 5.0)
check_answer(type(a + 2.0), float)

a = a + 1.0
check_answer(a, 4.0)
check_answer(type(a), float)

if b == None:
  print "Correct"
else:
  print "Wrong"

check_answer(a == 5.0, False)
check_answer(type(a == 5.0), bool)

b = 10
c = b > 9
check_answer(c, True)
check_answer(type(c), bool)
