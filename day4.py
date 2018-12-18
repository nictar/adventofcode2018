from collections import defaultdict

def day_4(fl):
    data = sorted(fl.split('\n')[:-1])
    guards = defaultdict(int)
    minutes = defaultdict(int)
    curr_guard = None

    for line in data:
        # parse information about the line
        words = line.split()
        minute = int(words[1].split(':')[1][:-1])
        asleep = True if 'falls asleep' in line else False
        guard = words[3][1:] if len(words) > 4 else None

        if guard is not None:
            # reading a 'Guard' line
            curr_guard = guard
            start_sleep = 0
        else:
            if asleep:
                start_sleep = minute
            else:
                # aggregate time spent sleeping
                guards[curr_guard] += (minute - start_sleep)
                for min_ in range(start_sleep, minute):
                    minutes[(curr_guard, min_)] += 1

    # chosen guard is the one with the highest sleeping time (ironic)
    chosen_guard = max(guards, key=guards.get)

    most = 0
    for (g, m), v in minutes.items():
        if g == chosen_guard:
            if v > most:
                most = v
                chosen_minute = m

    print('Part 1: ' + str(int(chosen_guard) * chosen_minute))


if __name__ == "__main__":
    # filename = 'test_input.txt'
    filename = 'day4_input.txt'
    fl = open(filename, 'r')
    day_4(fl.read())
    fl.close()
