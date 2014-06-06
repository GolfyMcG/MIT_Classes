import types

def check_answer(question, answer):
  if question is type(None) or question is None:
    if answer == "NoneType" or answer == "None":
      print "Correct"
    else:
      print "Wrong"
  elif isinstance(question, types.FunctionType):
    if answer == "Function":
      print "Correct"
    else:
      print "Wrong"
  else:
    if question == answer:
      print "Correct"
    else:
      print "Wrong"
