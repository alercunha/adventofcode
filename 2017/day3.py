import math


def part1(data):
    # the depth of the spiral for a given n is the square root of n /2
    # the bottom right diagonal is (depth * 2 + 1) ^ 2
    # 37  36  35  34  33  32  31
    # 38  17  16  15  14  13  30
    # 39  18   5   4   3  12  29
    # 40  19   6   1   2  11  28
    # 41  20   7   8   9  10  27
    # 42  21  22  23  24  25  26
    # 43  44  45  46  47  48  49
    sqrt = math.ceil(math.sqrt(data))
    if sqrt % 2 == 0:
        sqrt += 1
    # takes the distance between the number and the nearest axis
    # 3  2  1  0  1  2  3
    # 2  2  1  0  1  2  2
    # 1  1  1  0  1  1  1
    # 0  0  0  0  0  0  0
    # 1  1  1  0  1  1  1
    # 2  2  1  0  1  2  2
    # 3  2  1  0  1  2  3
    if sqrt == 1:
        dist = 0
    else:
        # distance to next diagonal counter clock wise
        dist_diag = math.fabs(data - sqrt * sqrt) % (sqrt - 1)
        # distance to axis
        dist = int(math.fabs(dist_diag - int(sqrt / 2)))
    return int(dist + (sqrt - 1) / 2)


def spiral():
    # return i,j in spiral
    # (-2, 2)  (-1, 2)  (0, 2)  (1, 2)  (2, 2)
    # (-2, 1)  (-1, 1)  (0, 1)  (1, 1)  (2, 1)
    # (-2, 0)  (-1, 0)  (0, 0)  (1, 0)  (2, 0)
    # (-2,-1)  (-1,-1)  (0,-1)  (1,-1)  (2,-1)
    # (-2,-2)  (-1,-2)  (0,-2)  (1,-2)  (2,-2)
    def ij_spiral(stop=0, _i=0, _j=0, _d=1):
        if _d > stop > 0:
            return
        _i += 1  # move right
        yield (_i, _j)
        for i in range(_d * 2 - 1):
            _j += 1  # move up
            yield (_i, _j)
        for i in range(_d * 2):
            _i -= 1  # move left
            yield (_i, _j)
        for i in range(_d * 2):
            _j -= 1  # move down
            yield (_i, _j)
        for i in range(_d * 2):
            _i += 1  # move right
            yield (_i, _j)
        for pos in ij_spiral(stop, _i, _j, _d + 1):
            yield pos

    data = {
        (0, 0): 1
    }
    yield 1
    gen = ij_spiral()
    while True:
        i, j = next(gen)
        # use ij_spiral(1) to calculate nearby neighbors
        result = sum(data.get((i + di, j + dj), 0) for di, dj in ij_spiral(1))
        data[(i, j)] = result
        yield result


def part2(data):
    gen = spiral()
    last = 0
    while last < data:
        last = next(gen)
    return last


if __name__ == '__main__':
    assert(part1(1) == 0)
    assert(part1(12) == 3)
    assert(part1(23) == 2)
    assert(part1(1024) == 31)
    print(part1(325489))

    known = [1, 1, 2, 4, 5, 10, 11, 23, 25, 26, 54, 57, 59, 122, 133, 142, 147, 304, 330, 351, 362, 747, 806]
    gen = spiral()
    values = [next(gen) for _ in range(len(known))]
    assert(known == values)
    print(part2(325489))
