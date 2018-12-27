from collections import defaultdict
import copy
import string

def day7(fl):
    # parse input and store its information
    node_tuples = []
    for line in fl:
        p = line.strip().split()[1]
        c = line.strip().split()[7]
        node_tuples.append((p,c))

    graph = Graph(node_tuples)
    topo = graph.topo_sort()
    t = graph.topo_distributed()

    print(f'Part 1: {"".join([x.value for x in topo])}')
    print(f'Part 2: {t}')

class Graph():
    def __init__(self, node_tuples):
        self.nodes = []
        self.make_graph(node_tuples)

    def make_graph(self, node_tuples):
        for node in node_tuples:
            pv = node[0]
            cv = node[1]
            pn = self.get_value_node(pv)
            cn = self.get_value_node(cv)

            if pn:
                if cn:
                    pn.add_child(cn)
                else:
                    cn = Node(cv)
                    pn.add_child(cn)
                    self.nodes.append(cn)
            else:
                pn = Node(pv)
                if cn:
                    pn.add_child(cn)
                    self.nodes.append(pn)
                else:
                    cn = Node(cv)
                    pn.add_child(cn)
                    self.nodes.append(pn)
                    self.nodes.append(cn)

    def get_value_node(self, value):
        for node in self.nodes:
            if node.value == value:
                return node
        return None

    def topo_sort(self):
        output = []
        ready = []

        # find nodes that are already ready to begin
        nodes_copy = copy.deepcopy(self.nodes)
        for node in nodes_copy:
            if not node.parents:
                ready.append(node)

        # Kahn's algorithm
        while ready:
            # alphabetically sort the nodes
            p = sorted(ready, key=lambda c: c.value)[0]

            ready.remove(p)
            output.append(p)
            for child in p.children:
                child.parents.remove(p)
                if not child.parents:
                    ready.append(child)

        return output

    def topo_distributed(self):
        alphabet = list(string.ascii_uppercase)
        num_workers = 5
        time_offset = 60

        # initialise the workers
        workers = {}
        for i in range(num_workers):
            workers[i] = []

        # find works that are already ready to begin
        ready = []
        nodes_copy = copy.deepcopy(self.nodes)
        for node in nodes_copy:
            if not node.parents:
                ready.append(node)

        time = 0
        output = []
        ongoing = []
        while ready or ongoing:
            # assign ready work to available workers
            for i in range(num_workers):
                if ready:
                    if not workers[i]:
                        p = sorted(ready, key=lambda c: c.value)[0]
                        workers[i].extend([p] * (alphabet.index(p.value)+1+time_offset))
                        ready.remove(p)
                        ongoing.append(p)
                else:
                    break

            # check if any of the workers is done with their assigned work
            for i in range(num_workers):
                if len(workers[i]) == 1:
                    done = workers[i].pop()
                    ongoing.remove(done)
                    output.append(done)

                    for child in done.children:
                        child.parents.remove(done)
                        if not child.parents:
                            ready.append(child)

            # continue doing unfinished work
            for i in range(num_workers):
                if workers[i]:
                    workers[i].pop()

            time += 1

        return time

class Node():
    def __init__(self, value=None):
        self.value = value
        self.parents = []
        self.children = []

    def add_child(self, c):
        self.children.append(c)
        c.parents.append(self)


if __name__ == "__main__":
    filename = 'input_files/day7_input.txt'
    fl = open(filename, 'r')
    day7(fl)
    fl.close()
