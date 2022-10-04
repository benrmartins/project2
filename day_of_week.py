import stdio
import sys

# Takes in the put into a int variable
m = int(sys.argv[1])
d = int(sys.argv[2])
y = int(sys.argv[3])

# Equation that turns the variables into a number that represents a day
y0 = int(y - (14 - m) // 12)
x0 = int(y0 + y0//4 - y0//100 + y0//400)
m0 = int(m + 12 * ((14 - m) // 12) - 2)
dow = int((d + x0 + 31 * m0//12) % 7)

# Displays the day according to the equation
if dow == 0:
    stdio.writeln("Sunday")
elif dow == 1:
    stdio.writeln("Monday")
elif dow == 2:
    stdio.writeln("Tuesday")
elif dow == 3:
    stdio.writeln("Wednesday")
elif dow == 4:
    stdio.writeln("Thursday")
elif dow == 5:
    stdio.writeln("Friday")
elif dow == 6:
    stdio.writeln("Saturday")
else:
    stdio.writeln("Error")
