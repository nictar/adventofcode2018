def part_1(file_object):
    total_freq = 0

    for line in file_object:
        total_freq += parse_frequency(line)

    print('Total frequency of input (part 1): ' + str(total_freq))


def part_2(file_object):
    print('First duplicate frequency (part 2): ')


def parse_frequency(line):
    curr_sign = line.strip()[0]
    curr_freq = int(line.strip()[1:])

    freq = curr_freq if curr_sign == '+' else (-1 * curr_freq)
    return freq


if __name__ == "__main__":
    filename = 'input.txt'
    fl = open(filename, 'r')
    part_1(fl)
    part_2(fl)
    fl.close()
