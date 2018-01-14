from day10 import knot_hash


def defrag(input):
    hashes = [knot_hash('{0}-{1}'.format(input, i)) for i in range(128)]
    return [
        bin(int(i, 16))[2:].zfill(128)
        for i in hashes
    ]


def part1(input):
    bins = defrag(input)
    return sum(sum(i == '1' for i in list(j)) for j in bins)


def part2(input):
    bins = [list(i.replace('1', '#')) for i in defrag(input)]
    count = 0

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def spread(x, y, v):
        for m in moves:
            _x, _y = x + m[0], y + m[1]
            if 0 <= _x < 128 and 0 <= _y < 128 and bins[_y][_x] == '#':
                bins[_y][_x] = v
                spread(_x, _y, v)

    for y in range(len(bins)):
        for x in range(len(bins[y])):
            if bins[y][x] == '#':
                count += 1
                bins[y][x] = count
                spread(x, y, count)

    return count


if __name__ == '__main__':
    assert(part1('flqrgnkx') == 8108)
    print(part1('ljoxqyyw'))

    assert(part2('flqrgnkx') == 1242)
    print(part2('ljoxqyyw'))
