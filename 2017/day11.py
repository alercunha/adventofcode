class Node(object):
    def __init__(self, n=None, val=None):
        self._n = None
        self.p = None
        self.n = n
        self.val = val

    @property
    def n(self):
        return self._n

    @n.setter
    def n(self, next_node):
        self._n = next_node
        if self._n:
            self._n.p = self

    def next_val(self):
        return self.n.val if self.n else None

    def prev_val(self):
        return self.p.val if self.p else None

    def insert(self, val):
        self.n = Node(self.n, val)
        return self.n

    def jump(self, length):
        curr = self
        if length == 0:
            return self
        for _ in range(abs(length)):
            curr = curr.n if length > 0 else curr.p
            if curr is None:
                return None
        return curr

    def size(self):
        count = 0
        curr = self
        while curr.n:
            count += 1
            curr = curr.n
        return count

    def __iter__(self):
        curr = self
        while curr.n:
            yield curr.n.val
            curr = curr.n

    def get_tuple(self):
        return tuple(self)

    def __nonzero__(self):
        return True


rules = [
    (['ne', 'sw'], []),
    (['ne', 'n', 'nw'], ['n']),
    (['ne', 'se', 's'], ['se']),
    (['se', 'nw'], []),
    (['se', 's', 'sw'], ['s']),
    (['se', 'ne', 'n'], ['ne']),
    (['nw', 'se'], []),
    (['nw', 'n', 'ne'], ['n']),
    (['nw', 'sw', 's'], ['sw']),
    (['sw', 'ne'], []),
    (['sw', 's', 'se'], ['s']),
    (['sw', 'nw', 'n'], ['nw']),
    (['n', 's'], []),
    (['n', 'ne', 'se'], ['ne']),
    (['n', 'nw', 'sw'], ['nw']),
    (['s', 'n'], []),
    (['s', 'se', 'ne'], ['se']),
    (['s', 'sw', 'nw'], ['sw']),
]


def transform(values):
    head = Node()
    tail = head
    for v in values:
        tail = tail.insert(v)
    return head


def find_comb(head):
    for k, v in rules:
        if k[0] == head.val:
            count = 2
            curr = head
            if len(k) > 2:
                while curr.next_val() == k[1]:
                    count += 1
                    curr = curr.n
            if curr.next_val() == k[-1]:
                return count, v
    return 0, []


def shrink(head):
    found = True
    while found:
        curr = head
        found = False
        while curr and curr.n:
            count, replace = find_comb(curr.n)
            if count > 0:
                curr.n = curr.jump(count).n
                for _ in range(len(replace) * (count - 1)):
                    curr.insert(replace[0])
                curr = curr.jump(-2) or head
                found = True
            else:
                curr = curr.n
    return head


def parse(input):
    return transform([s.strip() for s in input.split(',') if s.strip()])


def part1(input):
    head = parse(input)
    shrink(head)
    return head.size()


def part2(input):
    vals = [s.strip() for s in input.split(',') if s.strip()]
    top = 0

    while top < len(vals):
        head = transform(vals)
        top = max(shrink(head).size(), top)
        vals = vals[0:-1]
        print('{0}:{1}'.format(top, len(vals)))

    return top

if __name__ == '__main__':
    assert(part1('ne, ne, ne') == 3)
    assert(shrink(parse('ne, ne, ne')).get_tuple() == ('ne', 'ne', 'ne'))
    assert(part1('ne, ne, sw, sw') == 0)
    assert(shrink(parse('ne, ne, sw, sw')).get_tuple() == ())
    assert(part1('ne, ne, s, s') == 2)
    assert(shrink(parse('ne, ne, s, s')).get_tuple() == ('se', 'se'))
    assert(part1('ne, ne, s, s, s') == 3)
    assert(shrink(parse('ne, ne, s, s, s')).get_tuple() == ('se', 'se', 's'))
    assert(part1('se, sw, se, sw, sw') == 3)
    assert(shrink(parse('se, sw, se, sw, sw')).get_tuple() == ('s', 's', 'sw'))
    assert(part1('se, s, sw, sw, s, se') == 4)
    assert(shrink(parse('se, s, sw, sw, s, se')).get_tuple() == ('s', 's', 's', 's'))
    assert(part1('n, ne, ne, se, s') == 3)
    assert(shrink(parse('n, ne, ne, se, s')).get_tuple() == ('ne', 'ne', 'se'))

    with open('day11.in', 'r') as fh:
        data = fh.read().strip()
    print(part1(data))

    assert(part2('ne, ne, ne') == 3)
    assert(part2('ne, ne, sw, sw') == 2)
    assert(part2('ne, ne, s, s') == 2)
    assert(part2('ne, ne, s, s, s') == 3)
    assert(part2('se, sw, se, sw, sw') == 3)
    assert(part2('se, s, sw, sw, s, se') == 4)

    print(part2(data))
