import sys

class CpuSimulator:
    def __init__(self):
        self.buffer = list()
        self.buffer_value = 0
        self.register = 1
        self.cycles_remaining = 0

    def queue_instr(self, instr, value = 0):
        self.buffer.append((instr, int(value)))

    def __process(self):
        if self.cycles_remaining == 0:
            self.register += self.buffer_value

            if len(self.buffer) > 0:
                instruction, value = self.buffer[0]
                self.buffer.pop(0)

                if instruction == 'addx':
                    self.cycles_remaining = 2
                elif instruction == 'noop':
                    self.cycles_remaining = 1

                self.buffer_value = value

        self.cycles_remaining -= 1

    def tick(self, num_ticks = 1):
        for i in range(int(num_ticks)):
            self.__process()

    def get_register(self):
        return self.register


def p10a():

    INITIAL = 20
    INTERVAL = 40

    simulator = CpuSimulator()
    
    solution = 0

    with open(sys.argv[1], 'r') as f:
        for line in f:
            line_split = line.split()

            if len(line_split) > 1:
                instr, value = line_split
                simulator.queue_instr(instr, value)
            else:
                instr = line_split[0]
                simulator.queue_instr(instr, 0)

    # Dejamos que se procese la cantidad inicial de veces
    simulator.tick(INITIAL)
    local_value = simulator.get_register()
    score = INITIAL * local_value

    print(f"Ciclo {INITIAL}: {local_value}. (+{score})")

    solution += score

    # Vamos contando cada uno de los intervalos

    for j in range(1,6):
        num_cycle = INITIAL + INTERVAL * j
        
        simulator.tick(INTERVAL)
        
        local_value = simulator.get_register()
        score = local_value * num_cycle
        print(f"Ciclo {num_cycle}: {local_value}. (+{score})")

        solution += score

    print("Solución:", solution)


def p10b():
    simulator = CpuSimulator()
    
    solution = 0

    with open(sys.argv[1], 'r') as f:
        for line in f:
            line_split = line.split()

            if len(line_split) > 1:
                instr, value = line_split
                simulator.queue_instr(instr, value)
            else:
                instr = line_split[0]
                simulator.queue_instr(instr, 0)

    for i in range(6):
        for j in range(40):
            simulator.tick()

            if abs(simulator.get_register() - j) > 1:
                print(".", end="")
            else:
                print("#", end="")

        print("")


if __name__ == '__main__':
    p10b()
