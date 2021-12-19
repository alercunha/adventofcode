def parse_input(input):
    return [line.strip() for line in input.split('\n') if line.strip()]


def neighbors(i, j, width, height):
    if i > 0:
        yield i - 1, j
    if j > 0:
        yield i, j - 1
    if i < width - 1:
        yield i + 1, j
    if j < height - 1:
        yield i, j + 1


def find_lowest(data):
    width = len(data[0])
    height = len(data)
    for i in range(0, width):
        for j in range(0, height):
            val = int(data[j][i])
            n = [int(data[n_j][n_i]) for n_i, n_j in neighbors(i, j, width, height)]
            if all(x > val for x in n):
                yield i, j, val


def part1(input):
    data = parse_input(input)
    return sum(1 + val for _, _, val in find_lowest(data))


def map_basin(i, j, width, height, data, map):
    if data[j][i] != '9' and (i, j) not in map:
        map[(i, j)] = 1
        for n_i, n_j in neighbors(i, j, width, height):
            map_basin(n_i, n_j, width, height, data, map)


def part2(input):
    data = parse_input(input)
    width = len(data[0])
    height = len(data)
    basins = list()
    for i, j, val in find_lowest(data):
        map = {}
        map_basin(i, j, width, height, data, map)
        size = len(map)
        basins.append(size)
    basins.sort()
    return basins[-1] * basins[-2] * basins[-3]


if __name__ == '__main__':
    example = """
    2199943210
    3987894921
    9856789892
    8767896789
    9899965678
    """

    assert part1(example) == 15
    with open('day09.in', 'r') as fh:
       input = fh.read()
    print(part1(input))

    assert part2(example) == 1134
    print(part2(input))
