def compile(size, commands):
    idxs = [i for i in range(size)]
    for comm in commands:
        if comm[0] == 's':
            idxs = [idxs[(i + size - comm[1]) % size] for i in range(size)]
        elif comm[0] == 'x':
            idxs[comm[1]], idxs[comm[2]] = idxs[comm[2]], idxs[comm[1]]
    return 'r', idxs


def dance(size, input, rounds):
    memory = {}
    array = list('abcdefghijklmnopqrstuvwxyz'[0:size])

    commands = []
    mini_dance = []
    for comm in [i.strip() for i in input.split(',')]:
        if comm[0] == 's':
            mini_dance.append(('s', int(comm[1:])))
        elif comm[0] == 'x':
            va, vb = comm[1:].split('/')
            mini_dance.append(('x', int(va), int(vb)))
        elif comm[0] == 'p':
            commands.append(compile(size, mini_dance))
            mini_dance = []
            va, vb = comm[1:].split('/')
            commands.append(('p', va, vb))

    while rounds > 0:
        input = ''.join(array)
        if input in memory:
            array = memory[input]
        else:
            for comm in commands:
                if comm[0] == 'p':
                    a, b = array.index(comm[1]), array.index(comm[2])
                    array[a], array[b] = array[b], array[a]
                elif comm[0] == 'r':
                    array = [array[i] for i in comm[1]]
            memory[input] = array
        rounds -= 1

    return ''.join(array)


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
    print(part2(16, data, 1 * 1000 * 1000 * 1000))
