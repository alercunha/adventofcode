map_part1 = {
    'forward': lambda hor, depth, x: (hor + x, depth),
    'down': lambda hor, depth, x: (hor, depth + x),
    'up': lambda hor, depth, x: (hor, depth - x),
}


map_part2 = {
    'forward': lambda hor, depth, aim, x: (hor + x, depth + aim * x, aim),
    'down': lambda hor, depth, aim, x: (hor, depth, aim + x),
    'up': lambda hor, depth, aim, x: (hor, depth, aim - x),
}


def parse_input(input, map):
    for row in input.split('\n'):
        if row.strip():
            command, x = row.split()
            yield map[command], int(x)


def part1(input):
    h, d = 0, 0
    for func, x in parse_input(input, map_part1):
        h, d = func(h, d, x)
    return h * d


def part2(input):
    h, d, a = 0, 0, 0
    for func, x in parse_input(input, map_part2):
        h, d, a = func(h, d, a, x)
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

    assert part2(example) == 900
    print(part2(input))
