import sys

def p1():
    overlaps = 0

    with open(sys.argv[1], 'r') as f:
        for line in f:
            lst1, lst2 = line.split(',')
            min1, max1 = lst1.split('-')
            min2, max2 = lst2.split('-')

            min1, max1 = int(min1), int(max1)
            min2, max2 = int(min2), int(max2)

            print(f"({min1}, {max1}) \t ({min2}, {max2})")

            if (min1 <= min2 and max2 <= max1) or (min2 <= min1 and max1 <= max2):
                overlaps += 1

    return overlaps


def p2():
    overlaps = 0

    with open(sys.argv[1], 'r') as f:
        for line in f:
            lst1, lst2 = line.split(',')
            min1, max1 = lst1.split('-')
            min2, max2 = lst2.split('-')

            min1, max1 = int(min1), int(max1)
            min2, max2 = int(min2), int(max2)

            min_overlap = max(min1, min2)
            max_overlap = min(max1, max2)
            
            if min_overlap <= max_overlap:
                overlaps += 1

    return overlaps


# print(p1())
print(p2())
