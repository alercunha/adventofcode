from collections import Counter


def parse_input(input):
    return[int(i) for i in input.split(',')]


class Shoal:
    def __init__(self, fish):
        self.counter = Counter(fish)
        for i in range(0, 9):
            self.counter[i] = self.counter.get(i, 0)

    def count(self):
        return sum(self.counter.values())

    def epoch(self):
        for i in range(0, 9):
            self.counter[i - 1] = self.counter[i]
        # newborns
        self.counter[6] += self.counter[-1]
        self.counter[8] = self.counter[-1]
        self.counter[-1] = 0


def part1(input, steps):
    shoal = Shoal(parse_input(input))
    for _ in range(0, steps):
        shoal.epoch()
    return shoal.count()


if __name__ == '__main__':
    example = "3,4,3,1,2"

    assert part1(example, 18) == 26
    assert part1(example, 80) == 5934
    with open('day06.in', 'r') as fh:
        input = fh.read()
    print(part1(input, 80))

    assert part1(example, 256) == 26984457539
    print(part1(input, 256))
