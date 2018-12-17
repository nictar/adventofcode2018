from itertools import cycle

def day_1(fl):
    data = [int(x) for x in fl.split()]

    # Part 1
    print('Total frequency of input (part 1): ' + str(sum(data)))

    # Part 2
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
    filename = 'day1_input.txt'
    fl = open(filename, 'r')
    day_1(fl.read())
    fl.close()
