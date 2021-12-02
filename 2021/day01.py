def parse_input(input):
    return [int(i) for i in input.split() if i]


def part1(input):
    data = parse_input(input)
    return sum(1 if data[i] > data[i - 1] else 0 for i in range(1, len(data)))


if __name__ == '__main__':
    example1_input = """
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
    assert part1(example1_input) == 7
    with open('day01.in', 'r') as fh:
        day01_input = fh.read()
    print(part1(day01_input))
