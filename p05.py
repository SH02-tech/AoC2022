import sys
import re

def get_stacks(lines):
    indx = 0
    info_read = True
    reg = re.compile('(\[.\] | {4})')

    num_stacks = int(len(lines[0])/4)
    stacks = [ list() for i in range(num_stacks) ]

    while info_read and indx < len(lines):
        data = reg.findall(lines[indx])

        if data != []: 
            for i in range(int(len(data))):
                if data[i][0] == '[':
                    stacks[i].append(data[i])
            indx += 1
        else:
            info_read = False
    
    return stacks 


def get_orders(lines):
    orders = list()

    reg = re.compile("move [0-9]* from [0-9]* to [0-9]*")
    reg_num = re.compile("[0-9]+")

    for line in lines:
        if reg.search(line) is not None:
            numbers = reg_num.findall(line)
            orders.append([int(num) for num in numbers])

    return orders


def p5a(lines):
    answer = ""

    stacks = get_stacks(lines)
    orders = get_orders(lines)

    for order in orders:
        num_moved = order[0]
        origin = order[1]-1
        final = order[2]-1

        for i in range(num_moved):
            if stacks[origin] != []:
                val = stacks[origin][0]
                stacks[origin].pop(0)
                stacks[final].insert(0, val)


    for stack in stacks:
        if stack != []:
            answer += stack[0][1]
        else:
            answer += ' '

    return answer


def p5b(lines):
    answer = ""

    stacks = get_stacks(lines)
    orders = get_orders(lines)

    for order in orders:
        num_moved = order[0]
        origin = order[1]-1
        final = order[2]-1

        sublist = stacks[origin][0:num_moved]
        del stacks[origin][0:num_moved]
        stacks[final] = sublist + stacks[final]


    for stack in stacks:
        if stack != []:
            answer += stack[0][1]
        else:
            answer += ' '

    return answer


def main():
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
        # answer = p5a(lines)
        answer = p5b(lines)
        print(answer)


if __name__ == "__main__":
    main()
