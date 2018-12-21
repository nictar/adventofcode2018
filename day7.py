from collections import defaultdict
import copy
import string

def day_7(fl):
    # parse input and store its information
    node_tuples = []
    for line in fl:
        p = line.strip().split()[1]
        c = line.strip().split()[7]
        node_tuples.append((p,c))

    graph = Graph(node_tuples)
    topo = graph.topo_sort()
    t = graph.topo_distributed()
    # graph.print_graph()

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
        num_workers = 2
        time_offset = 0

        # prepare the workers
        workers = {}
        for i in range(num_workers):
            workers[i+1] = []

        output = []
        ready = []

        # find nodes that are already ready to begin
        nodes_copy = copy.deepcopy(self.nodes)
        for node in nodes_copy:
            if not node.parents:
                ready.append(node)

        time = 0

        # Kahn's algorithm
        while ready:
            # alphabetically sort the nodes
            for i in range(len(ready)):
                p = sorted(ready, key=lambda c: c.value)[i]
                workers[i+1].extend([p] * (alphabet.index(p.value)+1))

            ready.remove(p)
            output.append(p)
            for child in p.children:
                child.parents.remove(p)
                if not child.parents:
                    ready.append(child)
        
        return time

    def print_graph(self):
        """Prints each node with its parents and children."""
        for node in self.nodes:
            print(node.value, end=' ')
            print(f'p({[p.value for p in node.parents]})', end=' ')
            print(f'c({[c.value for c in node.children]})')

class Node():
    def __init__(self, value=None):
        self.value = value
        self.parents = []
        self.children = []

    def add_child(self, c):
        self.children.append(c)
        c.parents.append(self)


if __name__ == "__main__":
    # filename = 'day7_input.txt'
    filename = 'test_input.txt'
    fl = open(filename, 'r')
    day_7(fl)
    fl.close()
