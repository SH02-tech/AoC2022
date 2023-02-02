import sys

def get_values():
    matrix = list(list())

    with open(sys.argv[1], 'r') as f:
        for line in f:
            row = list()

            for ch in line[:-1]:
                row.append(int(ch))

            matrix.append(row)

    return matrix

def is_visible(matrix, pos_x, pos_y):
    visible = dict()

    visible['north'] = True
    visible['south'] = True
    visible['east'] = True
    visible['west'] = True

    length = len(matrix)
    local_size = matrix[pos_x][pos_y]

    for i in range(0, pos_x):
        if matrix[i][pos_y] >= local_size:
            visible['north'] = False

    for i in range(pos_x+1, length):
        if matrix[i][pos_y] >= local_size:
            visible['south'] = False

    for j in range(0, pos_y):
        if matrix[pos_x][j] >= local_size:
            visible['west'] = False

    for j in range(pos_y+1, length):
        if matrix[pos_x][j] >= local_size:
            visible['east'] = False

    return visible['north'] or visible['south'] or visible['east'] or visible['west']



def visible_area(matrix, pos_x, pos_y):
    length = len(matrix)
    local_value = matrix[pos_x][pos_y]

    dist_north = 1
    dist_east = 1
    dist_west = 1
    dist_south = 1

    stop = False

    while pos_y - dist_west > 0 and not stop:
        if matrix[pos_x][pos_y - dist_west] < local_value:
            dist_west += 1
        else:
            stop = True

    stop = False

    while pos_y+dist_east < length-1 and not stop:
        if matrix[pos_x][pos_y+dist_east] < local_value:
            dist_east += 1
        else:
            stop = True

    stop = False

    while pos_x - dist_north > 0 and not stop:
        if matrix[pos_x-dist_north][pos_y] < local_value:
            dist_north += 1
        else:
            stop = True

    stop = False

    while pos_x + dist_south < length-1 and not stop:
        if matrix[pos_x + dist_south][pos_y] < local_value:
            dist_south += 1
        else:
            stop = True

    return dist_north * dist_south * dist_east * dist_west


def p8a():
    solution = 0

    matrix = get_values()

    counter = 0
    length = len(matrix)

    for i in range(1, length-1):
        for j in range(1, length-1):
            if is_visible(matrix, i, j):
                counter += 1

    solution = counter + 4*(length-1)
    print(solution)


def p8b():
    solution = 0

    matrix = get_values()

    max_score = 0
    length = len(matrix)

    for i in range(1, length-1):
        for j in range(1, length-1):
            score = visible_area(matrix, i, j)
            print(f"Score by pos ({i}, {j}): {score})")
            max_score = max(max_score, score)

    print("Final score:", max_score)


def main():
    # p8a()
    p8b()

if __name__ == '__main__':
    main()
