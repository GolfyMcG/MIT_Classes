import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '../modules/'))

import checkers
import math

#This is just asking for me to create a function that calculates
# the shortest distance between a point and a line!
def pointDist(x1, y1, x2, y2):
  d1 = x2 - x1
  d2 = y2 - y1
  square_distance = d1**2 + d2**2
  distance = math.sqrt(square_distance)
  return distance

def perpDist(px, py, a, b, c):
  #Find the slope of the line
  #The equation a*x + b*y + c = 0 in point-intercept form is:
  # y = (-a/b)*x - c/b
  # slope = (-a/b)
  # perp_slope = (b/a)

  # Equation for new line
  cn = py - px*(b/a)
  # yn = (b/a)*xn + cn

  # Equation for old line
  # yo = (-a/b)*xo - (c/b)

  # Intersects where xn = xo = xs and yn = yo = ys
  # (b/a)*xs + cn = (-a/b)*xs - (c/b)
  # (b/a)*xs = -(a/b)*xs - (c/b) - cn
  # xs = (-(a/b)*xs - (c/b) - cn)/(b/a)
  # xs = -((a/b)**2)*xs - (c*a)/(b**2) - cn*(a/b)
  # xs*[1 + ((a/b)**2)] = - (c*a)/(b**2) - cn*(a/b)
  xs = (-(c*a)/(b**2) - cn*(a/b))/(1 + ((a/b)**2))

  yo = (-a/b)*xs - (c/b)

  # Round to the hundred's place
  shrt_distance = round(pointDist(xs, yo, px, py)*100)/100
  print shrt_distance
  return shrt_distance

question = perpDist(10, 0, 1, 1, 1)
checkers.check_answer(question, 7.81)
