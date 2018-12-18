def day_5(fl):
    data = fl.read().strip('\n')
    answer = ['.']

    for unit in data:
        x = answer[-1]
        if unit.swapcase() == x:
            answer.pop()
        else:
            answer.append(unit)

    print('Part 1: ' + str(len(answer)-1))


if __name__ == "__main__":
    filename = 'day5_input.txt'
    # filename = 'test_input.txt'
    fl = open(filename, 'r')
    day_5(fl)
    fl.close()
