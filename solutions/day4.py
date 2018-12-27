from collections import defaultdict

def day4(fl):
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

    # chosen guard according to strategy 1
    chosen_guard = max(guards, key=guards.get)

    # chosen minute according to strategy 1
    most = 0
    for (g, m), v in minutes.items():
        if g == chosen_guard:
            if v > most:
                most = v
                chosen_minute = m

    print('Part 1: ' + str(int(chosen_guard) * chosen_minute))

    # chosen guard and minute according to strategy 2
    chosen_guard, chosen_minute = max(minutes, key=minutes.get)
    print('Part 2: ' + str(int(chosen_guard) * chosen_minute))


if __name__ == "__main__":
    filename = 'input_files/day4_input.txt'
    fl = open(filename, 'r')
    day4(fl.read())
    fl.close()
