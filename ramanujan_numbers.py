import stdio
import sys

# took the vaalue from the terminal and stored it in an int variable
n = int(sys.argv[1])

# set value of a to 1
a = 1

# used nested while loops to produce the distinct positive integers
while(a * a * a) <= n:
    b = 1 + a
    while(a * a * a + b * b * b) <= n:
        c = 1 + a
        while(c * c * c) <= n:
            d = 1 + c
            while(c * c * c + d * d * d) <= n:
                x = a * a * a + b * b * b
                y = c * c * c + d * d * d
                if x == y:
                    # concatenated strings to match the example
                    stdio.write(str(x) + ' = ')
                    stdio.write(str(a) + '^3 ' "+ " + str(b) + '^3 ' + '= ')
                    stdio.writeln(str(c) + '^3 ' + "+ " + str(d) + '^3')
                d += 1
            c += 1
        b += 1
    a += 1
