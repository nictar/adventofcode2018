from collections import defaultdict

def day_11():
    PUZZLE_INPUT = 9221
    GRID_SIZE = 300

    grid = defaultdict(int)
    largest = defaultdict(int)

    for y in range(1, GRID_SIZE+1):
        for x in range(1, GRID_SIZE+1):

            # calculate the total area power of the current cell
            if not grid[(x, y)]:
                grid[(x, y)] = calculate_power(PUZZLE_INPUT, x, y)
            largest[(x, y)] += grid[(x, y)]

            area_power = calculate_area_power(PUZZLE_INPUT, grid, GRID_SIZE, x, y)
            if area_power is None:
                largest[(x, y)] = 0
            else:
                largest[(x, y)] += area_power

    print(f'Part 1: {max(largest, key=largest.get)}')


def calculate_area_power(grid_id, grid, grid_size, x, y):
    area_power = 0
    for sy in range(1,3):
        for sx in range(1,3):
            if x+sx > grid_size or y+sy > grid_size:
                return None

            if not grid[(x+sx, y+sy)]:
                grid[(x+sx, y+sy)] = calculate_power(grid_id, x+sx, y+sy)
            area_power += grid[(x+sx, y+sy)]
    return area_power


def calculate_power(grid_id, x, y):
    rack_id = x + 10
    power = (rack_id * y + grid_id) * rack_id
    power = int(str(power)[-3]) if len(str(power)) >= 3 else 0
    return power - 5


if __name__ == "__main__":
    day_11()
