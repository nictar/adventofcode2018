def part_1(file_object):
    total_freq = 0

    for line in file_object:
        total_freq += parse_frequency(line)

    print('Total frequency of input (part 1): ' + str(total_freq))


def part_2(file_object):
    cumulative_freq = 0
    duplicate_freq  = 0
    frequencies = []

    for line in file_object:
        cumulative_freq += parse_frequency(line)
        frequencies.append(cumulative_freq)

    adder = frequencies[-1]
    for freq in frequencies:
        new_freq = freq + adder
        if new_freq in frequencies:
            duplicate_freq = new_freq
            break
        frequencies.append(new_freq)

    print('First duplicate frequency (part 2): ' + str(duplicate_freq))


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
