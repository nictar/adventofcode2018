def part_1(fl):
    data = [int(x) for x in fl.split()]
    print('Total frequency of input (part 1): ' + str(sum(data)))


def part_2(file_object):
    cumulative_freq = 0
    duplicate_freq  = 0
    frequencies = []

    for line in file_object:
        cumulative_freq += int(line)
        frequencies.append(cumulative_freq)

    adder = frequencies[-1]
    for freq in frequencies:
        new_freq = freq + adder
        if new_freq in frequencies:
            duplicate_freq = new_freq
            break
        frequencies.append(new_freq)

    print('First duplicate frequency (part 2): ' + str(duplicate_freq))


if __name__ == "__main__":
    filename = 'input.txt'
    fl = open(filename, 'r')
    part_1(fl.read())
    # part_2(fl)
    fl.close()
