import stdio
import sys

# takes in the value from the terminal and into a variable
n = int(sys.argv[1])

# loops from 2 to the nth value
for i in range(2, n + 1):
    total = 0

    for j in range(1, i // 2 + 1):
        # checks if the i is divisible vy j
        if i % j == 0:
            # sets the total of the sum of divisors of i
            total += j
    if total == i:
        # displays i if its a perfect number
        stdio.writeln(i)
