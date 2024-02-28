def parse(input):
    return [list(s) for s in input.split('\n')]


moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def find(elevation, val):
    for j in range(len(elevation)):
        for i in range(len(elevation[j])):
            if elevation[j][i] == val:
                return (i, j)


def move_to(elevation, stack, dest):
    pos = stack[-1]
    if pos[1] < 0 or pos[1] > len(elevation):
        return False
    if pos[0] < 0 or pos[0] > len(elevation[0]):
        return False
    if elevation[pos[1]][pos[0]] == dest:
        return True
    for move in moves:
        next = (pos[0] + move[0], pos[1] + move[1])
        dist = ord(elevation[next[1]][next[0]]) - ord(elevation[pos[1]][pos[0]])
        if dist >= -1 and dist <= 1:
            new_stack = stack + pos
            found = move_to(elevation, new_stack, dest)
            return True
    return


def part1(elevation):
    start = find(elevation, 'S')
    stack = [start]
    found = []
    


if __name__ == '__main__':
    example1 = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""

    assert part1(parse(example1)) == 31

    with open('day12.in', 'r') as fh:
        input = fh.read().strip()
    
    print(part1(parse(input)))

    #assert part2(parse(example1)) == 2713310158

    #print(part2(parse(input)))
