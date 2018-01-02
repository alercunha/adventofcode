class Node:
    def __init__(self, n=None, val=None):
        self.n = n
        self.val = val

    def next_val(self):
        return self.n.val if self.n else None

    def insert(self, val):
        self.n = Node(self.n, val)
        return self.n

    def jump(self, length):
        for _ in range(length):
            self.n = self.n.n

reds = {
    ('ne', 'sw'): [],
    ('ne', 'n', 'nw'): ['n'],
    ('ne', 'se', 's'): ['se'],
    ('se', 'nw'): [],
    ('se', 's', 'sw'): ['s'],
    ('se', 'ne', 'n'): ['ne'],
    ('nw', 'se'): [],
    ('nw', 'n', 'ne'): ['n'],
    ('nw', 'sw', 's'): ['sw'],
    ('sw', 'ne'): [],
    ('sw', 's', 'se'): ['s'],
    ('sw', 'nw', 'n'): ['nw'],
    ('n', 's'): [],
    ('n', 'ne', 'se'): ['ne'],
    ('n', 'nw', 'sw'): ['nw'],
    ('s', 'n'): [],
    ('s', 'se', 'ne'): ['se'],
    ('s', 'sw', 'nw'): ['sw'],
}


def find_comb(head):
    for k, v in reds.items():
        if k[0] == head.val:
            count = 2
            curr = head
            while len(k) > 2 and curr.n and curr.next_val() == k[1]:
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
        while curr is not None and curr.n is not None:
            count, result = find_comb(curr.n)
            if count > 0:
                curr.jump(count)
                for _ in range(len(result) * (count - 1)):
                    curr.insert(result[0])
                found = True
            else:
                curr = curr.n
    return head


def parse(input):
    return transform([s.strip() for s in input.split(',') if s.strip()])


def transform(values):
    head = Node()
    tail = head
    for v in values:
        tail = tail.insert(v)
    return head


def get_tuple(head):
    if not head.n:
        return ()
    return (head.n.val,) + get_tuple(head.n)


def size(head):
    count = 0
    while head.n:
        count += 1
        head = head.n
    return count


def part1(input):
    head = parse(input)
    shrink(head)
    return size(head)


def part2(input):
    return 0


if __name__ == '__main__':
    assert(part1('ne, ne, ne') == 3)
    assert(get_tuple(shrink(parse('ne, ne, ne'))) == ('ne', 'ne', 'ne'))
    assert(part1('ne, ne, sw, sw') == 0)
    assert(get_tuple(shrink(parse('ne, ne, sw, sw'))) == ())
    assert(part1('ne, ne, s, s') == 2)
    assert(get_tuple(shrink(parse('ne, ne, s, s'))) == ('se', 'se'))
    assert(part1('ne, ne, s, s, s') == 3)
    assert(get_tuple(shrink(parse('ne, ne, s, s, s'))) == ('se', 'se', 's'))
    assert(part1('se, sw, se, sw, sw') == 3)
    assert(get_tuple(shrink(parse('se, sw, se, sw, sw'))) == ('s', 's', 'sw'))
    assert(part1('se, s, sw, sw, s, se') == 4)
    assert(get_tuple(shrink(parse('se, s, sw, sw, s, se'))) == ('s', 's', 's', 's'))
    with open('day11.in', 'r') as fh:
        data = fh.read().strip()
    print(size(parse(data)))
    print(part1(data))
