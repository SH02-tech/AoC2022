import sys
import numpy as np

fich = open(sys.argv[1])
max_values = [0,0,0]
sum = 0

for line in fich:
    if line != '\n':
        sum += int(line)
    else:
        if (sum > max_values[0]):
            max_values[0] = sum
        max_values.sort()
        sum = 0

print(np.sum(max_values))
