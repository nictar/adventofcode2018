from collections import defaultdict

def day_8(fl):
    data = list(map(int, [f for f in fl.readline().strip().split()]))

    child_count = [data[0]]
    meta_count = [data[1]]

    values = defaultdict(list)
    ref = ["root"]
    max_child = [child_count[0]]

    i = 2
    is_meta = False
    while i < len(data):
        if not is_meta:
            if child_count[-1] != 0:

                # add references to root's children and grandchildren
                if ref[-1] == "root":
                    ref.append(str(1 + max_child[-1] - child_count[-1]))
                else:
                    ref.append(ref[-1] + '.' + str(1 + max_child[-1] - child_count[-1]))

                child_count[-1] -= 1
                child_count.append(data[i])
                max_child.append(data[i])
                is_meta = True
            else:
                # add all of the metadata values
                if meta_count[-1] != 0:
                    values[ref[-1]].append(data[i])
                    meta_count[-1] -= 1

                # finally at the end of the current node, pop() everything
                if meta_count[-1] == 0:
                    meta_count.pop()
                    child_count.pop()
                    ref.pop()
                    max_child.pop()
        else:
            meta_count.append(data[i])
            is_meta = False
        i += 1
    
    part_1(values)
    p2 = 0
    for node in values["root"]:
        p2 += part_2(values, node)
    print(f'Part 2: {p2}')


def part_1(values):
    sum_ = 0
    for v in values.values():
        for x in v:
            sum_ += x
    print(f'Part 1: {sum_}')


def part_2(values, node):
    sum_ = 0
    child_found = False
    for x in values[str(node)]:
        # if a subchild node exists, find its value
        if values[str(node) + '.' + str(x)] != []:
            sum_ += part_2(values, str(node) + '.' + str(x))
        else:
            # otherwise, check if it references a non-existent child
            for k in values.keys():
                if str(node) + '.' in k and values[k] != []:
                    child_found = True
                    break
            # only add the metadata values if the current node has no children
            if not child_found:
                sum_ += x
                child_found = False

    return sum_


if __name__ == "__main__":
    filename = 'input_files/day8_input.txt'
    fl = open(filename, 'r')
    day_8(fl)
    fl.close()
