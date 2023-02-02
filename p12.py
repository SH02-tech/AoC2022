def saturate(low, up, number):
    if number < low:
        return low
    elif number > up:
        return up
    else:
        return number

def p12a():
    steps = 0
    board = []

    line = input()

    while line != '':
        board.append([ch for ch in line])

        line = input()

    n = len(board)

    start = (0,0)
    end = (0,0)

    for i in range(n):
        for j in range(len(board[i])):
            if board[i][j] == 'S':
                start = (i,j)
            elif board[i][j] == 'E':
                end = (i,j)

    accessible = {start}
    front = {start}

    while end not in accessible:
        new_front = set()

        for x,y in front:
            to_visit = list()

            n_columns = len(board[0])

            to_visit.append( (saturate(0, n-1, x-1), saturate(0, n_columns-1, y)) )
            to_visit.append( (saturate(0, n-1, x+1), saturate(0, n_columns-1, y)) )
            to_visit.append( (saturate(0, n-1, x), saturate(0, n_columns-1, y-1)) )
            to_visit.append( (saturate(0, n-1, x), saturate(0, n_columns-1, y+1)) )

            for elem in to_visit:
                if elem not in accessible and elem not in front:
                    previous = board[x][y]
                    new_x, new_y = elem
                    new = board[new_x][new_y]

                    if previous == 'S':
                        previous = 'a'
                    elif previous == 'E':
                        previous = 'z'

                    if new == 'S':
                        new = 'a'
                    elif new == 'E':
                        new = 'z'

                    if ord(previous) - ord(new) >= -1:
                        new_front.add(elem)


        accessible = accessible.union(front)
        front = new_front
        steps += 1

    return steps-1


def p12b():
    steps = 0
    board = []

    line = input()

    while line != '':
        board.append([ch for ch in line])

        line = input()

    n = len(board)

    start = set()
    end = (0,0)

    for i in range(n):
        for j in range(len(board[i])):
            if board[i][j] == 'S' or board[i][j] == 'a':
                start.add((i,j))
            elif board[i][j] == 'E':
                end = (i,j)

    accessible = start
    front = start

    while end not in accessible:
        new_front = set()

        for x,y in front:
            to_visit = list()

            n_columns = len(board[0])

            to_visit.append( (saturate(0, n-1, x-1), saturate(0, n_columns-1, y)) )
            to_visit.append( (saturate(0, n-1, x+1), saturate(0, n_columns-1, y)) )
            to_visit.append( (saturate(0, n-1, x), saturate(0, n_columns-1, y-1)) )
            to_visit.append( (saturate(0, n-1, x), saturate(0, n_columns-1, y+1)) )

            for elem in to_visit:
                if elem not in accessible and elem not in front:
                    previous = board[x][y]
                    new_x, new_y = elem
                    new = board[new_x][new_y]

                    if previous == 'S':
                        previous = 'a'
                    elif previous == 'E':
                        previous = 'z'

                    if new == 'S':
                        new = 'a'
                    elif new == 'E':
                        new = 'z'

                    if ord(previous) - ord(new) >= -1:
                        new_front.add(elem)


        accessible = accessible.union(front)
        front = new_front
        steps += 1

    return steps-1


if __name__ == '__main__':
    steps = p12b()
    print(steps)
