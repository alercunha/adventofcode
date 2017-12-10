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


if __name__ == '__main__':
    assert(part1(1) == 0)
    assert(part1(12) == 3)
    assert(part1(23) == 2)
    assert(part1(1024) == 31)
    print(part1(325489))
