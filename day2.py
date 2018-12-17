from collections import defaultdict
from itertools import combinations

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

    # Part 2
    test = combinations(box_ids, 2)
    for a, b in test:
        differ_counter = 0
        differ_index = 0

        # check each character from the string combination
        x = list(zip(a, b))
        for i in range(len(x)):
            if differ_counter > 1:
                # too many different characters; next combination!
                break

            # if the two characters differ, increase the counter and remember the index
            l1, l2 = x[i]
            if l1 != l2:
                differ_counter += 1
                differ_index = i

        # found the two strings with only one different character
        if differ_counter == 1:
            answer = [a[i] for i in range(len(a)) if i != differ_index]
            print(*answer, sep='')
            break


if __name__ == "__main__":
    filename = 'day2_input.txt'
    fl = open(filename, 'r')
    day_2(fl.read())
    fl.close()
