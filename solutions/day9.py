from collections import defaultdict, deque

def day9(fl):
    data = fl.readline().strip().split()
    max_player = int(data[0])

    # uncomment the line below for part 1, and comment the line below it
    max_marble = int(data[-2])

    # uncomment the line below for part 2, and comment the line above
    # max_marble = int(data[-2]) * 100

    scores = defaultdict(int)

    # change answer to use deque instead of implementing manual list rotation
    # courtesy of /u/marcusandrews
    circle = deque([0])

    for marble_count in range(1, max_marble+1):
        if marble_count % 23 == 0:
            circle.rotate(7)
            scores[marble_count % max_player] += marble_count + circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(marble_count)

    print(f'Highscore: {max([v for v in scores.values()])}')


if __name__ == "__main__":
    filename = 'input_files/day9_input.txt'
    fl = open(filename, 'r')
    day9(fl)
    fl.close()
