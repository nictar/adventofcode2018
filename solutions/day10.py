def day10(fl):
    # max number of seconds checked ahead
    iteration_threshold = 11000

    # parse data from input file
    positions = []
    velocities = []
    for point in fl:
        point = point.replace('<', ' ').split()
        positions.append([int(point[1][:-1]), int(point[2][:-1])])
        velocities.append((int(point[4][:-1]), int(point[5][:-1])))

    # find the iteration (second) at which the area of the stars is smallest.
    # this is based on the assumption that when a legible message is formed, all
    # of the stars are closest to one another.
    iterations = []
    for i in range(iteration_threshold):
        minx = min(positions[j][0] + i * velocities[j][0] for j in range(len(positions)))
        miny = min(positions[j][1] + i * velocities[j][1] for j in range(len(positions)))
        maxx = max(positions[j][0] + i * velocities[j][0] for j in range(len(positions)))
        maxy = max(positions[j][0] + i * velocities[j][0] for j in range(len(positions)))
        iterations.append((i, maxx + maxy - minx - miny))
    smallest_iteration = min(iterations, key=lambda d: d[1])

    # draw the stars, adjusting their positions to fit into a normal terminal width
    grid = [[' '] * 65 for x in range(11)]
    print(f'Part 1: ')
    for i in range(len(positions)):
        x = positions[i][0] + smallest_iteration[0] * velocities[i][0] - 110
        y = positions[i][1] + smallest_iteration[0] * velocities[i][1] - 135
        grid[y][x] = '*'

    for g in grid:
        print(''.join(g))

    print(f'Part 2: {smallest_iteration[0]}')


if __name__ == "__main__":
    filename = 'input_files/day10_input.txt'
    fl = open(filename, 'r')
    day10(fl)
    fl.close()
