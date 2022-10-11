import stdio
import sys

n = int(sys.argv[1])

# sets values to the first three numbers of the Fibonacci sequence
a = 1
b = 1
i = 3

# loops until the you find the number of the sequence you inputed
while i <= n:

    # finds the next numbers of the Fibonacci sequence
    temp = b
    b = a + b
    a = temp
    i += 1

stdio.writeln(b)
