import stdio
import sys

# takes in the number from the terminal into a int variable
n = int(sys.argv[1])

dragon = "F"
nogard = "F"

# loops until i gets to the nth value
for i in range(1, n + 1):
    # saves the value of dragon into a temporary variable
    temp = dragon
    # Adds the curve to the dragon
    dragon = dragon + "L" + nogard
    nogard = temp + "R" + nogard

# displays the curve of the dragon determined by the input
stdio.writeln(dragon)
