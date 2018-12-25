from collections import deque

def day_12(fl):
    GENERATIONS = 20

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
    for _ in range(GENERATIONS):
        new_plants = []
        for i in range(plants[0]-2, plants[-1]+2):

            # inspired by /u/sophiebits
            window = ''.join('#' if i+j in plants else '.' for j in [-2, -1, 0, 1, 2])
            if window in rules:
                new_plants.append(i)
        plants = new_plants

    print(f'Part 1: {sum(plants)}')

if __name__ == "__main__":
    with open('day12_input.txt') as fl:
    # with open('test_input.txt') as fl:
        day_12(fl)
