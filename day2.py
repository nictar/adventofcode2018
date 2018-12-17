from collections import defaultdict

def day_2(fl):
    box_ids = [x for x in fl.split()]
    two_counter = 0
    three_counter = 0

    for box_id in box_ids:
        seen = defaultdict(int)
        for letter in box_id:
            seen[letter] += 1

        if 2 in seen.values():
            two_counter += 1
        if 3 in seen.values():
            three_counter += 1

    print(two_counter * three_counter)


if __name__ == "__main__":
    filename = 'day2_input.txt'
    fl = open(filename, 'r')
    day_2(fl.read())
    fl.close()
