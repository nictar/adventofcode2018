def day_8(fl):
    data = list(map(int, [f for f in fl.readline().strip().split()]))
    
    sum_ = 0
    child_count = [data[0]]
    meta_count = [data[1]]

    i = 2
    is_meta = False
    while i < len(data):
        if not is_meta:
            if child_count[-1] != 0:
                child_count[-1] -= 1
                child_count.append(data[i])
                is_meta = True
            else:
                if meta_count[-1] != 0:
                    sum_ += data[i]
                    meta_count[-1] -= 1
                if meta_count[-1] == 0:
                    meta_count.pop()
                    child_count.pop()
        else:
            meta_count.append(data[i])
            is_meta = False
        i += 1
    
    print(f'Part 1: {sum_}')


if __name__ == "__main__":
    filename = 'day8_input.txt'
    # filename = 'test_input.txt'
    fl = open(filename, 'r')
    day_8(fl)
    fl.close()
