def reverse(array, start, length):
    if length <= 1:
        return
    end = (start + length - 1) % len(array)
    array[start], array[end] = array[end], array[start]
    reverse(array, (start + 1) % len(array), length - 2)


def knot_hash_round(data, lengths, rounds=1):
    pos = 0
    skip = 0
    for _ in range(rounds):
        for l in lengths:
            reverse(data, pos, l)
            pos = (pos + l + skip) % len(data)
            skip += 1
    return data


def part1(input1, input2):
    data = [int(i.strip()) for i in input1.split(',') if i.strip()]
    lengths = [int(i.strip()) for i in input2.split(',') if i.strip()]
    result = knot_hash_round(data, lengths)
    return result[0] * result[1]


def knot_hash(input):
    data = list(range(256))
    lengths = [ord(i) for i in input] + [17, 31, 73, 47, 23]
    result = knot_hash_round(data, lengths, 64)
    dense_hash = [reduce(lambda x, y: x ^ y, result[i * 16:(i + 1) * 16]) for i in range(16)]
    return ''.join(format(i, '02x') for i in dense_hash)


def part2(input):
    return knot_hash(input)


if __name__ == '__main__':
    assert(part1('0, 1, 2, 3, 4', '3, 4, 1, 5') == 12)
    day10_length = '230,1,2,221,97,252,168,169,57,99,0,254,181,255,235,167'
    print(part1(', '.join([str(i) for i in range(256)]), day10_length))

    assert(part2('') == 'a2582a3a0e66e6e86e3812dcb672a272')
    assert(part2('AoC 2017') == '33efeb34ea91902bb2f59c9920caa6cd')
    assert(part2('1,2,3') == '3efbe78a8d82f29979031a4aa0b16a9d')
    assert(part2('1,2,4') == '63960835bcdc130f0b66d7ff4f6a5a8e')
    print(part2(day10_length))
