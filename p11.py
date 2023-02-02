import sys
import re

WORRY_FACTOR = 1/3
total_factor = 1 # shall be the product of all the tests

class Monkey:
    def __init__(self, items, lambda_op, test, true_monkey, false_monkey):
        self.items = items
        self.lambda_op = lambda_op
        self.test = test
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey

    def throw(self):
        if len(self.items) == 0:
            return (-1,-1)

        item = self.items.pop(0)
        #new_worry_item = int(self.lambda_op(item) * WORRY_FACTOR)
        new_worry_item = int(self.lambda_op(item)) % total_factor 
        next_monkey = self.true_monkey if (new_worry_item % self.test == 0) else self.false_monkey

        return (next_monkey, new_worry_item) 

    def new_item(self, item):
        self.items.append(item)

    def get_list(self):
        return self.items


class MonkeyGroup:
    def __init__(self):
        self.monkeys = list()
        self.items_examined = list()

    def add_monkey(self, monkey):
        self.monkeys.append(monkey)
        self.items_examined.append(0)

    def perform_round(self):
        idx = 0
        for monkey in self.monkeys:
            num_items = int(len(monkey.get_list()))
            self.items_examined[idx] += num_items
            
            for i in range(num_items):
                monkey_idx, item = monkey.throw()
                self.monkeys[monkey_idx].new_item(item)

            idx += 1

    def print_status(self):
        idx = 0

        for monkey in self.monkeys:
            print(f"Monkey {idx} inspected items {self.items_examined[idx]} times.")
            idx += 1

    def business_level(self):
        lst = self.items_examined
        max1 = max(lst)

        lst.remove(max1)
        max2 = max(lst)

        return max1*max2

def read_monkey(file_type):

    num_reg = re.compile(r'[0-9]+')
    op_reg = re.compile(r'=.*')
    
    text = file_type.readline()
    text = file_type.readline()

    items = [int(elem) for elem in num_reg.findall(text)]

    text = file_type.readline()
    aux, p1, op, p2 = op_reg.findall(text)[0].split()
    
    lambda_op = lambda x: x

    if op == '*':
        if p1 == p2:
            lambda_op = lambda x: x*x
        else:
            lambda_op = lambda x: x*int(p2)
    else:
        if p1 == p2:
            lambda_op = lambda x: x+x
        else:
            lambda_op = lambda x: x+int(p2)

    text = file_type.readline()
    test = int(num_reg.findall(text)[0])
    
    global total_factor
    total_factor *= test

    text = file_type.readline()
    true_monkey = int(num_reg.findall(text)[0])

    text = file_type.readline()
    false_monkey = int(num_reg.findall(text)[0])

    text = file_type.readline()

    return Monkey(items, lambda_op, test, true_monkey, false_monkey)

def p11a():
    monkey_group = MonkeyGroup()

    with open(sys.argv[1], 'r') as f:
        for i in range(8):
            monkey = read_monkey(f)
            monkey_group.add_monkey(monkey)

    for i in range(10000):
        monkey_group.perform_round()

    print(monkey_group.business_level())

if __name__ == '__main__':
    p11a()

#    monkey_group = MonkeyGroup()
#    
#    monkey_group.add_monkey(Monkey([79,98], lambda x: x*19, 23, 2, 3))
#    monkey_group.add_monkey(Monkey([54,65,75,74], lambda x: x+6, 19, 2, 0))
#    monkey_group.add_monkey(Monkey([79,60,97], lambda x: x*x, 13, 1, 3))
#    monkey_group.add_monkey(Monkey([74], lambda x: x+3, 17, 0, 1))
#
#    for i in range(10000):
#        monkey_group.perform_round()
#    
#    monkey_group.print_status()
#    print(monkey_group.business_level())
