def parse_input(input):
    return [
        [
            [int(x) for x in i.split(',')]
            for i in r.strip().split(' -> ')
        ]
        for r in input.split('\n') if r.strip()
    ]


def do_range(start, end):
    x1, y1 = start
    x2, y2 = end
    yield x1, y1
    while (x1, y1) != (x2, y2):
        x1 += 1 if x2 > x1 else -1 if x2 < x1 else 0
        y1 += 1 if y2 > y1 else -1 if y2 < y1 else 0
        yield x1, y1


def scan(data):
    floor = {}
    for vent in data:
        for i, j in do_range(vent[0], vent[1]):
            val = floor.get((i, j), 0)
            floor[(i, j)] = val + 1
    return sum([1 for k, v in floor.items() if v > 1])


def part1(input):
    data = parse_input(input)
    filtered = [v for v in data if v[0][0] == v[1][0] or v[0][1] == v[1][1]]
    return scan(filtered)


def part2(input):
    data = parse_input(input)
    return scan(data)


if __name__ == '__main__':
    example = """
    0,9 -> 5,9
    8,0 -> 0,8
    9,4 -> 3,4
    2,2 -> 2,1
    7,0 -> 7,4
    6,4 -> 2,0
    0,9 -> 2,9
    3,4 -> 1,4
    0,0 -> 8,8
    5,5 -> 8,2
    """

    assert part1(example) == 5
    with open('day05.in', 'r') as fh:
        input = fh.read()
    print(part1(input))

    assert part2(example) == 12
    print(part2(input))
