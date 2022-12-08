import sys

def solve_subscore(elem):
    subscore = 0

    if elem.isupper():
        subscore += ord(elem) - ord('A') + 27
    else:
        subscore += ord(elem) - ord('a') + 1 

    return subscore


def p1(fich_name):

    fich = open(fich_name, 'r')

    score = 0

    for line in fich:
        midlength = int(len(line)/2)
        comp1, comp2 = set(line[:midlength]), set(line[midlength:])
        common = comp1.intersection(comp2)

        subscore = 0

        for elem in common:
            subscore += solve_subscore(elem)

        score += subscore

    fich.close()
    
    return score


def p2(fich_name):
    score = 0

    with open(fich_name, 'r') as fich:
        lines = fich.readlines()

        for i in range(int(len(lines)/3)):
            l1 = set(lines[3*i])
            l2 = set(lines[3*i + 1])
            l3 = set(lines[3*i + 2])

            aux = l1.intersection(l2)
            aux = aux.intersection(l3)

            aux.remove('\n')

            for elem in aux:
                score += solve_subscore(elem)

    return score

#print(p1(sys.argv[1]))
print(p2(sys.argv[1]))
