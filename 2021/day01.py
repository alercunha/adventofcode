def parse_input(input):
    return [int(i) for i in input.split() if i]


def part1(input):
    data = parse_input(input)
    return sum(1 if data[i] > data[i - 1] else 0 for i in range(1, len(data)))


def part2(input):
    data = parse_input(input)

    def measure(i):
        return data[i] + data[i + 1] + data[i + 2]

    count = [1 if measure(i) > measure(i - 1) else 0 for i in range(1, len(data) - 2)]
    return sum(count)


if __name__ == '__main__':
    example_input = """
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
    assert part1(example_input) == 7
    with open('day01.in', 'r') as fh:
        day01_input = fh.read()
    print(part1(day01_input))

    assert part2(example_input) == 5
    print(part2(day01_input))
