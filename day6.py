import sys
from collections import defaultdict

def day_6(fl):
    # parse and store coordinate data
    coordinates = defaultdict(int)
    for i, row in enumerate(fl):
        x, y = row.split(', ')
        coordinates[(int(x), int(y))] = i+1

    # determine the borders of the grid
    min_x = min(x for x,y in coordinates.keys())
    min_y = min(y for x,y in coordinates.keys())
    max_x = max(x for x,y in coordinates.keys())
    max_y = max(y for x,y in coordinates.keys())

    # keep a record of the 'infinite' coordinates
    infinites = [-1]
    for k,v in coordinates.items():
        if k[0] == min_x or k[0] == max_x or k[1] == min_y or k[1] == max_y:
            infinites.append(v)

    # mark each individual location on the grid with the nearest coordinate
    locations = defaultdict(int)
    for x in range(max_x+1):
        for y in range(max_y+1):
            smallest_dist = sys.maxsize
            nearest_coor = None
            for k,v in coordinates.items():
                curr_dist = dist((x,y), k)
                if curr_dist < smallest_dist:
                    smallest_dist = curr_dist
                    nearest_coor = v

                # mark this location if it's equidistant to >1 coordinates 
                elif curr_dist == smallest_dist:
                    nearest_coor = -1

            locations[(x, y)] = nearest_coor

    # calculate area of each non-infinite coordinate
    areas = defaultdict(int)
    for v in locations.values():
        if v not in infinites:
            areas[v] += 1

    print(f'Part 1: {max(v for v in areas.values())}')


def dist(c1, c2):
    """Returns the Manhattan distance between two coordinate points."""
    return abs(c2[0]-c1[0]) + abs(c2[1]-c1[1])


if __name__ == "__main__":
    filename = 'day6_input.txt'
    # filename = 'test_input.txt'
    fl = open(filename, 'r')
    day_6(fl)
    fl.close()
