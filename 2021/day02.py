map = {
    'forward': lambda hor, depth, x: (hor + x, depth),
    'down': lambda hor, depth, x: (hor, depth + x),
    'up': lambda hor, depth, x: (hor, depth - x),
}


def parse_input(input):
    for row in input.split('\n'):
        if row.strip():
            command, x = row.split()
            yield map[command], int(x)


def part1(input):
    h = 0
    d = 0
    for func, x in parse_input(input):
        h, d = func(h, d, x)
    return h * d


if __name__ == '__main__':
    example = """
    forward 5
    down 5
    forward 8
    up 3
    down 8
    forward 2
    """
    assert part1(example) == 150
    with open('day02.in', 'r') as fh:
        input = fh.read()
    print(part1(input))
