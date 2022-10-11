import stdio
import sys

# sets int variable to the input in the terminal
n = int(sys.argv[1])
p = int(sys.argv[2])

totalPower = 0
# loops untill from 1 to the value in the terminal
for i in range(1, n + 1):
    # adds the power starting a 1
    totalPower += i ** p

stdio.writeln(totalPower)
