from collections import Counter


class Node:
    def __init__(self, name):
        self.connections = list()
        self.name = name
        self.small = name[0].islower()

    def find_all_paths(self, dest, valid_path_func):
        paths = list()
        self.__find_all_paths(dest, list(), paths, valid_path_func)
        return paths

    def __find_all_paths(self, dest, current, paths, valid_path_func):
        current = current + [self.name]
        if self.name == dest:
            paths.append(current)
            return
        for node in self.connections:
            if valid_path_func(node, current):
                node.__find_all_paths(dest, current, paths, valid_path_func)


def parse_input(input):
    nodes = {}

    def get_node(name):
        node = nodes.get(name, None)
        if not node:
            node = Node(name)
            nodes[name] = node
        return node

    for row in [r.strip() for r in input.split('\n') if r.strip()]:
        a, b = [get_node(i) for i in row.split('-')]
        a.connections.append(b)
        b.connections.append(a)

    return nodes['start']


def part1(input):
    start = parse_input(input)

    def valid_path(node, path):
        return not (node.small and node.name in path)

    paths = start.find_all_paths('end', valid_path)
    return len(paths)


def part2(input):
    start = parse_input(input)

    def valid_path(node, path):
        if node.name == 'start':
            return False
        if path[-1] == 'end':
            return False
        if node.small:
            if node.name not in path:
                return True
            c = Counter(path)
            return not any(v == 2 for k, v in c.items() if k[0].islower())
        return True

    paths = start.find_all_paths('end', valid_path)
    return len(paths)


if __name__ == '__main__':
    example1 = """
    start-A
    start-b
    A-c
    A-b
    b-d
    A-end
    b-end
    """

    assert part1(example1) == 10

    example2 = """
    dc-end
    HN-start
    start-kj
    dc-start
    dc-HN
    LN-dc
    HN-end
    kj-sa
    kj-HN
    kj-dc
    """

    assert part1(example2) == 19

    example3 = """
    fs-end
    he-DX
    fs-he
    start-DX
    pj-DX
    end-zg
    zg-sl
    zg-pj
    pj-he
    RW-he
    fs-DX
    pj-RW
    zg-RW
    start-pj
    he-WI
    zg-he
    pj-fs
    start-RW
    """

    assert part1(example3) == 226

    with open('day12.in', 'r') as fh:
       input = fh.read()
    print(part1(input))

    assert part2(example1) == 36
    assert part2(example2) == 103
    assert part2(example3) == 3509
    print(part2(input))
