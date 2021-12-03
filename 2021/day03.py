def parse_input(input):
    return input.split()


def most_common_bits(data):
    count_1 = [0] * len(data[0])
    for row in data:
        for idx, c in enumerate(row):
            if c == '1':
                count_1[idx] += 1
    return ''.join('1' if c > len(data) / 2 else '0' for c in count_1)


def part1(input):
    data = parse_input(input)
    result = most_common_bits(data)
    gamma = int(result, 2)
    epsilon = int(''.join('1' if c == '0' else '0' for c in result), 2)
    return gamma * epsilon


def bit_criteria(data, idx, expected_bit):
    if len(data) == 1:
        return data
    count_1 = 0
    for row in data:
        if row[idx] == '1':
            count_1 += 1
    threshold = len(data) / 2

    if count_1 == threshold:
        common = expected_bit
    elif expected_bit == 0:
        common = 1 if count_1 < threshold else 0
    else:
        common = 0 if count_1 < threshold else 1

    filtered = filter(lambda a: a[idx] == str(common)[0], data)
    return bit_criteria(list(filtered), idx + 1, expected_bit)


def part2(input):
    data = parse_input(input)
    oxygen = bit_criteria(data, 0, 1)[0]
    co2 = bit_criteria(data, 0, 0)[0]
    return int(oxygen, 2) * int(co2, 2)


if __name__ == '__main__':
    example = """
    00100
    11110
    10110
    10111
    10101
    01111
    00111
    11100
    10000
    11001
    00010
    01010
    """
    assert part1(example) == 198
    with open('day03.in', 'r') as fh:
        input = fh.read()
    print(part1(input))

    assert part2(example) == 230
    print(part2(input))