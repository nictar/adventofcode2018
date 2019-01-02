def day13(fl):
    carts = []
    for y, row in enumerate(fl):
        for x, col in enumerate(row):
            if col in "^v<>":
                direction = {
                    "^": "up",
                    "v": "down",
                    "<": "left",
                    ">": "right"
                }[col]
                carts.append(Cart((x, y), direction))

    for cart in carts:
        print(cart.coordinate)


class Cart:
    def __init__(self, coordinate, direction):
        self.coordinate = coordinate
        self.direction = direction

    def move(self):
        pass

    def turn(self):
        pass


if __name__ == "__main__":
    # with open('input_files/day13_input.txt') as fl:
    with open('solutions/test_input.txt') as fl:
        day13(fl)
