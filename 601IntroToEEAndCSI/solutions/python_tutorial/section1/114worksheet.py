import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '../modules/'))

import math
import checkers

checkers.check_answer(type(3 + 5.0), float)
checkers.check_answer(type(5/2), int)
checkers.check_answer(type(5/2 == 5/2.0), bool)
checkers.check_answer(type(5/2.0), float)
checkers.check_answer(type(round(2.6)), float)
checkers.check_answer(type(int(2.6)), int)
checkers.check_answer(type(math.floor(2.6)), float)
checkers.check_answer(type(2.0 + 5.0), float)
checkers.check_answer(type( 5 * 2 == 5.0 * 2.0), bool)
