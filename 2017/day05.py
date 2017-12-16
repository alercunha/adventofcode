def part1(input):
    offsets = [int(i.strip()) for i in input.split(' ') if i.strip()]
    pos = 0
    count = 0
    while pos < len(offsets):
        offsets[pos] += 1
        pos = pos + offsets[pos] - 1
        count += 1
    return count


def part2(input):
    offsets = [int(i.strip()) for i in input.split(' ') if i.strip()]
    pos = 0
    count = 0
    while pos < len(offsets):
        if offsets[pos] < 3:
            offsets[pos] += 1
            pos = pos + offsets[pos] - 1
        else:
            offsets[pos] -= 1
            pos = pos + offsets[pos] + 1
        count += 1
    return count


if __name__ == '__main__':
    assert(part1('0 3 0 1 -3') == 5)
    with open('day5.in', 'r') as fh:
        data = fh.read().replace('\n', ' ')
    print(part1(data))

    assert(part2('0 3 0 1 -3') == 10)
    print(part2(data))
