import sys
from collections import defaultdict

def day6(fl):
    # parse and store coordinate data
    coordinates = []
    for row in fl:
        x,y = row.strip().split(', ')
        coordinates.append((int(x), int(y)))

    # determine the 'size' of the grid
    max_x = max(x for x,y in coordinates)
    max_y = max(y for x,y in coordinates)

    # count the 'area' of each coordinate, taking note of 'infinite' ones
    areas = defaultdict(int)
    infinites = [(-1,-1)]
    safe = 0                    # part 2: count number of 'safe' points
    for x in range(max_x+1):
        for y in range(max_y+1):
            nearest = get_nearest((x,y), coordinates)

            # part 2
            total_dist = sum(dist((x,y), c) for c in coordinates)
            if total_dist < 10000:
                safe += 1

            # exclude coordinates that are closest to infinite points
            if x in (0, max_x) or y in (0, max_y):
                infinites.append(nearest)
                if nearest in areas:
                    del areas[nearest]
            else:
                areas[nearest] += 1

    print(f'Part 1: {max(v for k,v in areas.items() if k not in infinites)}')
    print(f'Part 2: {safe}')


def get_nearest(point, coordinates):
    """Returns the nearest coordinate to `point` from the list of coordinates."""
    n = [(dist(point, c), c) for c in coordinates]
    n.sort()

    if n[0][0] < n[1][0]:
        return n[0][1]
    return (-1,-1)


def dist(c1, c2):
    """Returns the Manhattan distance between two coordinate points."""
    return abs(c2[0]-c1[0]) + abs(c2[1]-c1[1])


if __name__ == "__main__":
    filename = 'input_files/day6_input.txt'
    fl = open(filename, 'r')
    day6(fl)
    fl.close()
