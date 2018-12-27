from collections import defaultdict

def day_3(fl):
    overlaps = 0
    area = defaultdict(int)
    ids = defaultdict(int)
    intersect = defaultdict(bool)

    for line in fl:
        # parse the information about the claim
        id_  = int(line.split()[0][1:])
        x, y = line.split()[2].split(',')
        x, y = int(x), int(y[:-1])
        width, height = line.split()[3].split('x')
        width, height = int(width), int(height)

        for i in range(width):
            for j in range(height):
                area[(x+i), (y+j)] += 1

                if ids[(x+i), (y+j)] == 0:
                    ids[(x+i), (y+j)] = id_
                    intersect[id_] = False if intersect[id_] == False else True
                else:
                    intersect[id_] = True
                    intersect[ids[(x+i), (y+j)]] = True

    # Part 1
    for v in area.values():
        if v > 1:
            overlaps += 1
    print('Part 1: ' + str(overlaps))

    # Part 2
    for k, v in intersect.items():
        if not v:
            print('Part 2: ' + str(k))
            return


if __name__ == "__main__":
    filename = 'input_files/day3_input.txt'
    fl = open(filename, 'r')
    day_3(fl)
    fl.close()
