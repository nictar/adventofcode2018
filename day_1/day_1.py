from itertools import cycle

def part_1(fl):
    data = [int(x) for x in fl.split()]
    print('Total frequency of input (part 1): ' + str(sum(data)))


def part_2(fl):
    data = [int(x) for x in fl.split()]
    duplicate_freq = 0

    cumulative_freq = 0
    seen = {0}
    for freq in cycle(data):
        cumulative_freq += freq
        if cumulative_freq in seen:
            duplicate_freq = cumulative_freq
            break
        seen.add(cumulative_freq)

    print('First duplicate frequency (part 2): ' + str(duplicate_freq))


if __name__ == "__main__":
    filename = 'input.txt'
    fl = open(filename, 'r')
    part_1(fl.read())
    fl.seek(0)
    part_2(fl.read())
    fl.close()
