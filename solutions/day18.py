from collections import defaultdict

def day_18(fl):
    acres = defaultdict(int)

    for line in fl:
        for acre in line.strip():
            acres[acre] += 1

    print(acres)

if __name__ == "__main__":
    filename = 'input_files/day18_input.txt'
    fl = open(filename, 'r')
    day_18(fl)
    fl.close()
