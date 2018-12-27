def day_5(fl):
    data = fl.read().strip('\n')
    print('Part 1: ' + str(react_polymer(data)))

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    # courtesy of /u/andreyrmg (holy Python list comprehension)
    shortest = min(react_polymer(unit for unit in data if unit.lower() != letter) for letter in alphabet)
    print('Part 2: ' + str(shortest))


def react_polymer(string):
    answer = ['.']

    # one pointer keeps on moving forward, meanwhile the other one refers back
    # to the stack, popping items as necessary if a duplicate after a duplicate
    # is found.
    for unit in string:
        x = answer[-1]
        if unit.swapcase() == x:
            answer.pop()
        else:
            answer.append(unit)
    
    return len(answer) - 1


if __name__ == "__main__":
    filename = 'input_files/day5_input.txt'
    fl = open(filename, 'r')
    day_5(fl)
    fl.close()
