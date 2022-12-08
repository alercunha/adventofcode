def parse(input):
    lines = input.split('\n')
    line = lines.pop(0)
    column_count = int((len(line) + 1) / 4)
    stacks = [list() for _ in range(column_count)]
    while not line.strip().startswith('1'):
        for i in range(0, column_count):
            if line[i * 4 + 1] != ' ':
                stacks[i].append(line[i * 4 + 1])
        line = lines.pop(0)
    lines.pop(0)
    
    moves = []
    for line in lines:
        moves.append(line.replace('move ', '').replace(' from ', ',').replace(' to ', ',').split(','))

    return stacks, [list(map(int, i)) for i in moves]


def execute_moves_9000(input):
    stacks = input[0]
    for move in input[1]:
        for i in range(move[0]):
            head = stacks[move[1] - 1].pop(0)
            stacks[move[2] - 1].insert(0, head)


def part1(input):
    execute_moves_9000(input)
    return ''.join([s[0] for s in input[0]])


def execute_moves_9001(input):
    stacks = input[0]
    for move in input[1]:
        for i in range(move[0]):
            head = stacks[move[1] - 1].pop(0)
            stacks[move[2] - 1].insert(i, head)


def part2(input):
    execute_moves_9001(input)
    return ''.join([s[0] for s in input[0]])


if __name__ == '__main__':
    example1 = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

    parsed_example1 = parse(example1)
    assert parsed_example1[0] == [['N', 'Z'], ['D', 'C', 'M'], ['P']]
    assert parsed_example1[1][0] == [1, 2, 1]
    assert part1(parsed_example1) == 'CMZ'

    with open('day05.in', 'r') as fh:
        input = fh.read()
    
    print(part1(parse(input)))

    parsed_example1 = parse(example1)
    assert part2(parsed_example1) == 'MCD'

    print(part2(parse(input)))
