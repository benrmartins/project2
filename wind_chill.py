import stdio
import sys

# takes in the values in the terminal and stores it into a float variable
t = float(sys.argv[1])
v = float(sys.argv[2])

# Checks if t and v has the correct input
if t > 50:
    stdio.writeln("Value of t must be <= 50 F")

elif v <= 3:
    stdio.writeln("Value of v must be > 3 mph")

# uses the equation to calculate to find wind chill
else:
    w = 35.74 + (0.6215 * t) + ((0.4275 * t) - 35.75) * (v ** 0.16)
    stdio.writeln(w)
