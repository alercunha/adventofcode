import functools


def parse_input(input):
    return[int(i) for i in input.split(',')]


def find_min_cost(points, cost_func):
    last_sum = cost_func(points, 0)

    for i in range(1, points[-1]):
        s = cost_func(points, i)
        if s > last_sum:
            return last_sum
        last_sum = s
    return last_sum


def part1(input):
    points = parse_input(input)
    points.sort()

    def cost(p, s):
        return sum([abs(i - s) for i in p])

    return find_min_cost(points, cost)


def part2(input):
    points = parse_input(input)
    points.sort()

    @functools.lru_cache(maxsize=None)
    def fact(i):
        if i == 0:
            return 0
        return fact(i - 1) + i

    def cost(p, s):
        return sum([fact(abs(i - s)) for i in p])

    return find_min_cost(points, cost)


if __name__ == '__main__':
    example = "16,1,2,0,4,2,7,1,2,14"

    assert part1(example) == 37
    with open('day07.in', 'r') as fh:
        input = fh.read()
    print(part1(input))

    print(part2(input))
