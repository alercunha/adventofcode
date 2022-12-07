def parse(input):
    return [i.strip().split(' ') for i in input.strip().split('\n')]


def part1(input):
    score_map = {
        'X': (1, { 'C': 6, 'A': 3, 'B': 0 }),
        'Y': (2, { 'A': 6, 'B': 3, 'C': 0 }),
        'Z': (3, { 'B': 6, 'C': 3, 'A': 0 }),
    }

    score = 0
    for round in input:
        round_score = score_map[round[1]]
        score += round_score[0] + round_score[1][round[0]]

    return score


def part2(input):
    score_map = {
        'X': { 'A': 3, 'B': 1, 'C': 2 },
        'Y': { 'A': 3 + 1, 'B': 3 + 2, 'C': 3 + 3 },
        'Z': { 'A': 6 + 2, 'B': 6 + 3, 'C': 6 + 1 },
    }

    score = 0
    for round in input:
        score += score_map[round[1]][round[0]]

    return score


if __name__ == '__main__':
    example1 = """
    A Y
    B X
    C Z
    """
    
    assert parse(example1) == [['A', 'Y'], ['B', 'X'], ['C', 'Z']]

    assert part1(parse(example1)) == 15

    with open('day02.in', 'r') as fh:
        input = fh.read()

    print(part1(parse(input)))

    assert part2(parse(example1)) == 12

    print(part2(parse(input)))
