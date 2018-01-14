def nav(array, pos):
    size = len(array)
    for i in range(size):
        yield array[(i + pos) % size]


def dance(size, input, rounds):
    array = list('abcdefghijklmnopqrstuvwxyz'[0:size])
    pos = 0

    commands = []
    for comm in [i.strip() for i in input.split(',')]:
        if comm[0] == 's':
            commands.append(('s', int(comm[1:])))
        elif comm[0] == 'x':
            va, vb = comm[1:].split('/')
            commands.append(('x', int(va), int(vb)))
        elif comm[0] == 'p':
            va, vb = comm[1:].split('/')
            commands.append(('p', va, vb))

    while rounds > 0:
        for comm in commands:
            if comm[0] == 's':
                pos = (pos - comm[1])
                pos = size - (-pos % size)
            elif comm[0] == 'x':
                a, b = (comm[1] + pos) % size, (comm[2] + pos) % size
                array[a], array[b] = array[b], array[a]
            elif comm[0] == 'p':
                a, b = array.index(comm[1]), array.index(comm[2])
                array[a], array[b] = array[b], array[a]
        rounds -= 1

    return ''.join(nav(array, pos))


def part1(size, input):
    return dance(size, input, 1)


def part2(size, input, rounds):
    return dance(size, input, rounds)


if __name__ == '__main__':
    assert(part1(5, 's1, x3/4, pe/b') == 'baedc')

    with open('day16.in', 'r') as fh:
        data = fh.read().strip()
    print(part1(16, data))

    assert(part2(5, 's1, x3/4, pe/b', 2) == 'ceadb')
    #print(part2(16, data, 1 * 1000 * 1000 * 1000))
