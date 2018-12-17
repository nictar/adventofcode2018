def get_freq(file_object):
    total_freq = 0

    for line in file_object:
        curr_sign = line.strip()[0]
        curr_freq = int(line.strip()[1:])

        if curr_sign == '+':
            total_freq += curr_freq
        else:
            total_freq -= curr_freq

    print(total_freq)


filename = 'input.txt'
fl = open(filename, 'r')
get_freq(fl)
fl.close()
