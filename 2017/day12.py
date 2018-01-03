import re


class Pipe(object):
    def __init__(self, val):
        self.val = val
        self.conn = {}

    def connect(self, pipe):
        self.conn[pipe.val] = pipe
        pipe.conn[self.val] = self

    def get_connected(self):
        return self.conn.values()

    def walk(self):
        walked = set()
        self._walk(walked)
        return walked

    def _walk(self, walked):
        walked.add(self.val)
        for c in self.get_connected():
            if c.val not in walked:
                c._walk(walked)


def parse(input):
    lines = [l.strip() for l in input.split('\n') if l.strip()]
    pattern = '(\d+) <-> ([\d+, ]+)'
    pipes = {}

    def get_pipe(val):
        p = pipes.get(val, None)
        if not p:
            p = Pipe(val)
            pipes[val] = p
        return p

    for l in lines:
        groups = re.match(pattern, l).groups()
        pipe = get_pipe(int(groups[0]))
        for d in groups[1].split(','):
            val = int(d.strip())
            pipe.connect(get_pipe(val))
    return pipes


def part1(input, id):
    pipes = parse(input)
    pipe = pipes[id]
    walked = pipe.walk()
    return len(walked)


def part2(input):
    pipes = parse(input)
    combined = set()
    count = 0
    for k in pipes.keys():
        if k not in combined:
            pipe = pipes[k]
            walked = pipe.walk()
            combined = combined.union(walked)
            count += 1
    return count


if __name__ == '__main__':
    a = '''
    0 <-> 2
    1 <-> 1
    2 <-> 0, 3, 4
    3 <-> 2, 4
    4 <-> 2, 3, 6
    5 <-> 6
    6 <-> 4, 5
    '''
    assert(part1(a, 0) == 6)

    with open('day12.in', 'r') as fh:
        data = fh.read().strip()
    print(part1(data, 0))

    assert(part2(a) == 2)
    print(part2(data))
