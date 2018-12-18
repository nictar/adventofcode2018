from collections import defaultdict

def day_3(fl):
    overlaps = 0
    area = defaultdict(int)

    for line in fl:
        # parse the information about the claim
        x, y = line.split()[2].split(',')
        x, y = int(x), int(y[:-1])
        width, height = line.split()[3].split('x')
        width, height = int(width), int(height)

        for i in range(width):
            for j in range(height):
                area[(x+i), (y+j)] += 1

    for v in area.values():
        if v > 1:
            overlaps += 1
    print('Part 1: ' + str(overlaps))
    
    fl.seek(0)

    # Part 2
    for line in fl:
        # parse the information about the claim
        id_  = int(line.split()[0][1:])
        x, y = line.split()[2].split(',')
        x, y = int(x), int(y[:-1])
        width, height = line.split()[3].split('x')
        width, height = int(width), int(height)

        intersect = False
        for i in range(width):
            for j in range(height):
                if area[(x+i), (y+j)] > 1:
                    intersect = True
                    break
            if intersect:
                break

        if not intersect:
            print('Part 2: ' + str(id_))
            return


if __name__ == "__main__":
    filename = 'day3_input.txt'
    fl = open(filename, 'r')
    day_3(fl)
    fl.close()
