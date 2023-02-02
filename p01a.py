import sys

fich = open(sys.argv[1])
max_value = 0
sum = 0

for line in fich:
    if line != '\n':
        sum += int(line)
    else:
        max_value = max(max_value, sum)
        sum = 0

print(max_value)
