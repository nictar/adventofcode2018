def day_1(file_object):
    total_freq = 0

    for line in file_object:
        curr_sign = line.strip()[0]
        curr_freq = int(line.strip()[1:])

        if curr_sign == '+':
            total_freq += curr_freq
        else:
            total_freq -= curr_freq

    print('Total frequency of input (part 1): ' + str(total_freq))


if __name__ == "__main__":
    filename = 'input.txt'
    fl = open(filename, 'r')
    day_1(fl)
    fl.close()
