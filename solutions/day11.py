def day_11():
    PUZZLE_INPUT = 9221
    GRID_SIZE = 300

    # calculate and record the power of each cell in the grid
    grid = {}
    for x in range(1, GRID_SIZE+1):
        for y in range(1, GRID_SIZE+1):
            grid[(x, y)] = calculate_power(PUZZLE_INPUT, x, y)

    # setup the summed-area table
    sat = {}
    for x in range(1, GRID_SIZE+1):
        for y in range(1, GRID_SIZE+1):
            sat[(x, y)] = grid[(x, y)] + sat.get((x, y-1), 0) + sat.get((x-1, y), 0) - sat.get((x-1, y-1), 0)

    # calculate the largest total power of each cell's area
    largest_power = -1e6
    largest_area = ()
    largest_square = 0
    for x in range(1, GRID_SIZE+1):
        for y in range(1, GRID_SIZE+1):
            for square_size in range(1, GRID_SIZE):
                # to get the answer for part 1, instead of wrapping the lines
                # below in the for loop directly above this line, change `square_size` to 3 (3x3 square)
                if x+square_size > GRID_SIZE or y+square_size > GRID_SIZE:
                    continue
                area_power = sat.get((x-1, y-1), 0) + sat.get((x+square_size-1, y+square_size-1), 0) - sat.get((x-1, y+square_size-1), 0) - sat.get((x+square_size-1, y-1), 0)
                if area_power > largest_power:
                    largest_power = area_power
                    largest_area = (x, y)
                    largest_square = square_size

    print(largest_area, largest_square)


def calculate_power(grid_id, x, y):
    rack_id = x + 10
    power = (rack_id * y + grid_id) * rack_id
    power = int(str(power)[-3]) if len(str(power)) >= 3 else 0
    return power - 5


if __name__ == "__main__":
    day_11()
