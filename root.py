import math

import stdio
import sys

# takes in the value from the terminal and into a variable
k = int(sys.argv[1])
c = float(sys.argv[2])
epsilon = float(sys.argv[3])

t = c
# while loop that stops when the absolute value is less than epsilon
while abs(1 - c / math.pow(t, k)) > epsilon:
    # equation that finds the kth root of c
    t = t - (t ** k - c) / (k * t ** (k - 1))

stdio.writeln(t)
