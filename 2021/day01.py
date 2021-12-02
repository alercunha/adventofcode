def parse_input(input):
    return [int(i) for i in input.split() if i]


def part1(input):
    data = parse_input(input)
    return sum(1 if data[i] > data[i - 1] else 0 for i in range(1, len(data)))


def part2(input):
    data = parse_input(input)

    def measure(i):
        return sum(data[i:i+3])

    count = [1 if measure(i) > measure(i - 1) else 0 for i in range(1, len(data) - 2)]
    return sum(count)


if __name__ == '__main__':
    example = """
    199
    200
    208
    210
    200
    207
    240
    269
    260
    263
    """
    assert part1(example) == 7
    with open('day01.in', 'r') as fh:
        input = fh.read()
    print(part1(input))

    assert part2(example) == 5
    print(part2(input))
