import sys

def all_distinct(string):
    return len(set(string)) == len(string)

def p6a(string):
    KEYLENGTH = 14 

    indx = KEYLENGTH
    length = len(string)
    found = False

    while indx < length and not found:
        substr = string[indx-KEYLENGTH:indx]

        if all_distinct(substr):
            found = True
        else:
            indx += 1

    return indx


def main():
    with open(sys.argv[1], 'r') as f:
        string = f.readline()
        answer = p6a(string)
        print(answer)


if __name__ == '__main__':
    main()
