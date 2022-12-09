def parse(input):
    return [i.split() for i in input.split('\n')]


move_deltas = {
    'U': (0, -1),
    'D': (0, 1),
    'R': (1, 0),
    'L': (-1, 0),
}

tail_deltas = {
    (0, 2): (0, 1),
    (1, 2): (1, 1),
    (2, 2): (1, 1),
    (-1, 2): (-1, 1),
    (-2, 2): (-1, 1),

    (0, -2): (0, -1),
    (1, -2): (1, -1),
    (2, -2): (1, -1),
    (-1, -2): (-1, -1),
    (-2, -2): (-1, -1),

    (2, 0): (1, 0),
    (2, 1): (1, 1),
    (2, -1): (1, -1),
    (-2, 0): (-1, 0),
    (-2, 1): (-1, 1),
    (-2, -1): (-1, -1),
}

def move_head(head, direction):
    delta = move_deltas[direction]
    return (head[0] + delta[0], head[1] + delta[1])


def move_tail(head, tail):
    delta = (head[0] - tail[0], head[1] - tail[1])
    move = tail_deltas.get(delta, (0, 0))
    return (tail[0] + move[0], tail[1] + move[1])


def part1(moves):
    head = (0,0)
    tail = (0,0)
    space = {(0,0): '#'}
    for move in moves:
        for _ in range(int(move[1])):
            head = move_head(head, move[0])
            tail = move_tail(head, tail)
            space[tail] = '#'
    return len(space.items())


def part2(moves):
    knots = [(0,0) for _ in range(10)]
    space = {(0,0): '#'}
    for move in moves:
        for _ in range(int(move[1])):
            knots[0] = move_head(knots[0], move[0])
            for i in range(1, len(knots)):
                knots[i] = move_tail(knots[i-1], knots[i])
            space[knots[-1]] = '#'
    return len(space.items())


if __name__ == '__main__':
    example1 = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""

    assert part1(parse(example1)) == 13

    with open('day09.in', 'r') as fh:
        input = fh.read().strip()
    
    print(part1(parse(input)))

    assert part2(parse(example1)) == 1

    example2 = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""

    assert part2(parse(example2)) == 36

    print(part2(parse(input)))
