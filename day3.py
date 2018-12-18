def day_3(fl):
    data = [x for x in fl.split('\n')]
    overlaps = 0

    x_off, y_off, width, height = parse_line(data[0])

    print('Part 1: ' + str(overlaps))


def parse_line(line):
    offsets = line.split()[2].replace(':', ',')
    x_offset = int(offsets.split(',')[0])
    y_offset = int(offsets.split(',')[1])

    width = int(line.split()[3].split('x')[0])
    height = int(line.split()[3].split('x')[1])

    # print(x_offset)
    # print(y_offset)
    # print(width)
    # print(height)

    return (x_offset, y_offset, width, height)


if __name__ == "__main__":
    filename = 'day3_input.txt'
    fl = open(filename, 'r')
    day_3(fl.read())
    fl.close()
