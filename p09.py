import sys

SIZE = 3000
NUM_KNOTS = 10

class Rope:
    def __init__(self, num_knots, ini_x = SIZE/2, ini_y = SIZE/2):
        self.xcomponents = [int(ini_x) for i in range(num_knots)]
        self.ycomponents = [int(ini_y) for i in range(num_knots)]
        self.num_knots = num_knots

        self.quadrant = list(list())

        for i in range(SIZE):
            self.quadrant.append([False for i in range(SIZE)])

        self.__update_quadrant()


    def __update_next(self, i):
            diff_x = self.xcomponents[i-1] - self.xcomponents[i]
            diff_y = self.ycomponents[i-1] - self.ycomponents[i]

            norm_vect = max(abs(diff_x), abs(diff_y))
            
            if norm_vect > 1:
                if (self.xcomponents[i] == self.xcomponents[i-1]) or (self.ycomponents[i] == self.ycomponents[i-1]):
                    self.xcomponents[i] += int(diff_x / norm_vect)
                    self.ycomponents[i] += int(diff_y / norm_vect)
                else:
                    self.xcomponents[i] += int(diff_x / abs(diff_x))
                    self.ycomponents[i] += int(diff_y / abs(diff_y))

                if i < self.num_knots-1:
                    self.__update_next(i+1)

    def __update_quadrant(self):
        #print("Values:", self.xcomponents[self.num_knots-1], self.ycomponents[self.num_knots-1]) 
        self.quadrant[self.xcomponents[self.num_knots-1]][self.ycomponents[self.num_knots-1]] = True

    def move(self, direction):
        if (direction == 'R'):
            self.ycomponents[0] += 1
        elif (direction == 'L'):
            self.ycomponents[0] -= 1
        elif (direction == 'U'):
            self.xcomponents[0] -= 1
        elif (direction == 'D'):
            self.xcomponents[0] += 1

        self.__update_next(1)
        self.__update_quadrant()


    def count_visited_tail(self):
        counter = 0

        for i in range(SIZE):
            for j in range(SIZE):
                if self.quadrant[i][j]:
                    print('#', end='')
                    counter += 1
                else:
                    print('.', end='')
            print("\n", end='')

        return counter


def p9a():

    rope = Rope(NUM_KNOTS)

    with open(sys.argv[1], 'r') as f:
        for line in f:
            instruction, repetition = line.split()
            repetition = int(repetition)

            for i in range(repetition):
                rope.move(instruction)
    
    print(rope.count_visited_tail())


def main():
    p9a()

if __name__ == '__main__':
    main()
