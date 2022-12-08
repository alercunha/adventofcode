def is_unique(group):
    for i in range(len(group)):
        for j in range(len(group)):
            if i != j and group[i] == group[j]:
                return min(i, j)
    return -1


def find_marker(input, marker_length):
    group = input[0:marker_length]
    idx = is_unique(group)
    offset = 0
    while idx != -1:
        offset = offset + idx + 1
        group = input[offset: offset + marker_length]
        idx = is_unique(group)
    return offset + marker_length


def part1(input):
    return find_marker(input, 4)


def part2(input):
    return find_marker(input, 14)


if __name__ == '__main__':
    assert part1('mjqjpqmgbljsphdztnvjfqwrcgsmlb') == 7
    assert part1('bvwbjplbgvbhsrlpgdmjqwftvncz') == 5
    assert part1('nppdvjthqldpwncqszvftbrmjlhg') == 6
    assert part1('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg') == 10
    assert part1('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw') == 11

    with open('day06.in', 'r') as fh:
        input = fh.read().strip()
    
    print(part1(input))

    assert part2('mjqjpqmgbljsphdztnvjfqwrcgsmlb') == 19
    assert part2('bvwbjplbgvbhsrlpgdmjqwftvncz') == 23
    assert part2('nppdvjthqldpwncqszvftbrmjlhg') == 23
    assert part2('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg') == 29
    assert part2('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw') == 26

    print(part2(input))
