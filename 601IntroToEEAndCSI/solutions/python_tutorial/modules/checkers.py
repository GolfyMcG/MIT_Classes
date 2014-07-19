import types


def check_answer(question, answer, number=0):
  def print_check(value):
    if value:
      response = "Correct"
    else:
      response = "Wrong***"

    print `number` + ".) " + response

  if question is type(None) or question is None:
    if answer == "NoneType" or answer == "None":
      print_check(True)
    else:
      print_check(False)
  elif isinstance(question, types.FunctionType):
    if answer == "Function":
      print_check(True)
    else:
      print_check(False)
  else:
    if question == answer:
      print_check(True)
    else:
      print_check(False)
