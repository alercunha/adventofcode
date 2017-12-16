import re


def calculate_graph(input):
    lines = [l.strip() for l in input.split('\n') if l.strip()]
    pattern = '(\w+) \((\d+)\)( -> ([\w, ]+))?'
    graph = {}
    weights = {}
    for l in lines:
        groups = re.match(pattern, l).groups()
        weights[groups[0]] = int(groups[1])
        if groups[3]:
            children = [i.strip() for i in groups[3].split(',') if i.strip()]
            graph[groups[0]] = children
    return graph, weights


def find_root(graph):
    values = [i for v in graph.values() for i in v]
    roots = list(i for i in graph.keys() if i not in values)
    if len(roots) != 1:
        raise Exception('Can\'t have multiple roots')
    return roots[0]


def part1(input):
    graph, _ = calculate_graph(input)
    return find_root(graph)


class WrongWeight(Exception):
    def __init__(self, node, diff):
        super(Exception, self).__init__()
        self.node = node
        self.diff = diff


def find_diff(array):
    s = sorted(enumerate(array), key=lambda v: v[1])
    if s[0][1] == s[-1][1]:
        return None
    return s[0][0] if s[0][1] != s[1][1] else s[-1][0]


def get_weight(graph, weights, node):
    w = weights[node]
    children = graph.get(node, None)
    if children:
        sub_weights = [get_weight(graph, weights, c) for c in children]
        wrong = find_diff(sub_weights)
        if wrong is not None:
            raise WrongWeight(children[wrong], sub_weights[wrong] - sub_weights[(wrong + 1) % len(sub_weights)])
        return w + sum(sub_weights)
    return w


def part2(input):
    graph, weights = calculate_graph(input)
    root = find_root(graph)

    try:
        get_weight(graph, weights, root)
    except WrongWeight as ex:
        return weights[ex.node] - ex.diff


if __name__ == '__main__':
    a = """
    pbga (66)
    xhth (57)
    ebii (61)
    havc (66)
    ktlj (57)
    fwft (72) -> ktlj, cntj, xhth
    qoyq (66)
    padx (45) -> pbga, havc, qoyq
    tknk (41) -> ugml, padx, fwft
    jptl (61)
    ugml (68) -> gyxo, ebii, jptl
    gyxo (61)
    cntj (57)
    """
    assert(part1(a) == 'tknk')

    with open('day7.in', 'r') as fh:
        data = fh.read()
    print(part1(data))

    b = """
    pbga (66)
    xhth (57)
    ebii (61)
    havc (66)
    ktlj (57)
    fwft (72) -> ktlj, cntj, xhth
    qoyq (66)
    padx (45) -> pbga, havc, qoyq
    tknk (41) -> ugml, padx, fwft
    jptl (61)
    ugml (60) -> gyxo, ebii, jptl
    gyxo (61)
    cntj (57)
    """
    graph, weights = calculate_graph(b)
    root = find_root(graph)
    assert(get_weight(graph, weights, root) == 770)
    assert(part2(a) == 60)
    print(part2(data))
