from __future__ import division


def hashf(banks):
    return ' '.join([str(int(i)) for i in banks])


def redist(banks):
    size = len(banks)
    hist = {hashf(banks): 0}
    count = 0
    while True:
        ix, val = max(enumerate(banks), key=lambda v: v[1])
        banks[ix] = 0
        while val > 0:
            ix = (ix + 1) % size
            banks[ix] += 1
            val -= 1
        count += 1
        h = hashf(banks)
        if h in hist:
            break
        hist[h] = count
    return count, count - hist[h]


def part1(input):
    banks = [int(i.strip()) for i in input.split(',') if i.strip()]
    return redist(banks)[0]


def part2(input):
    banks = [int(i.strip()) for i in input.split(',') if i.strip()]
    return redist(banks)[1]


if __name__ == '__main__':
    assert(part1('0, 2, 7, 0') == 5)
    day6_input = '10, 3, 15, 10, 5, 15, 5, 15, 9, 2, 5, 8, 5, 2, 3, 6'
    print(part1(day6_input))

    assert(part2('0, 2, 7, 0') == 4)
    print(part2(day6_input))
