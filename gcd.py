import stdio
import sys

# gets a input from the terminal into a int variable
p = int(sys.argv[1])
q = int(sys.argv[2])

# loops until p is divisible by q
while (p % q) != 0:

    temp = q
    # sets q to the greatest common divisor
    q = p % q
    # sets p to the value of p
    p = temp

stdio.writeln(q)
