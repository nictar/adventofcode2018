def day12(fl):
    GENERATIONS = 150

    # parse the initial state
    initial = fl.readline().strip().split()[2]
    fl.readline()
    plants = [i for i in range(len(initial)) if initial[i] == '#']

    # parse the rules
    rules = []
    for rule in fl:
        rule = rule.strip().split()
        if rule[2] == '#':
            rules.append(rule[0])

    # check the state of each generation
    for g in range(1, GENERATIONS+1):
        new_plants = []
        for i in range(plants[0]-2, plants[-1]+2):

            # inspired by /u/sophiebits
            window = ''.join('#' if i+j in plants else '.' for j in [-2, -1, 0, 1, 2])
            if window in rules:
                new_plants.append(i)
        plants = new_plants

        # special stops at certain generations for part1 and part2, because
        # apparently for part2, a pattern emerges after a certain generation,
        # which could be used to simplify calculating its answer
        if g == 20:
            print(f'Part 1: {sum(plants)}')
        if g == 113:
            print(f'Part 2: {(5e10 - 113)*80 + sum(plants)}')
            break


if __name__ == "__main__":
    with open('input_files/day12_input.txt') as fl:
        day12(fl)
