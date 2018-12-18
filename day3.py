from collections import defaultdict

def day_3(fl):
    overlaps = 0

    for line in fl:
        # parse the x and y-offsets, and the width and height of the claim
        x, y = line.split()[2].split(',')
        x, y = int(x), int(y[:-1])
        width, height = line.split()[3].split('x')
        width, height = int(width), int(height)
        # print(str(x), str(y), str(width), str(height))

    print('Part 1: ' + str(overlaps))


if __name__ == "__main__":
    filename = 'test-input.txt'
    fl = open(filename, 'r')
    day_3(fl)
    fl.close()
