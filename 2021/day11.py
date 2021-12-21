def neighbors(i, j, width, height):
    if i > 0:
        yield i - 1, j
        if j > 0:
            yield i - 1, j - 1
        if j < height - 1:
            yield i - 1, j + 1
    if i < width - 1:
        yield i + 1, j
        if j > 0:
            yield i + 1, j - 1
        if j < height - 1:
            yield i + 1, j + 1
    if j > 0:
        yield i, j - 1
    if j < height - 1:
        yield i, j + 1


class Ocean:
    def __init__(self, floor) -> None:
        self.floor = floor
        self.flash_count = 0
        self.last_flash_count = 0
        self.step_count = 0
        self.size = len(self.floor) * len(self.floor[0])

    def step(self):
        self.floor = [[i + 1 for i in r] for r in self.floor]
        self.flash()
        self.reset()
        self.step_count += 1

    def flash(self):
        height = len(self.floor)
        width = len(self.floor[0])
        flashed = False
        for j in range(0, height):
            for i in range(0, width):
                if self.floor[j][i] > 9:
                    flashed = True
                    for n_i, n_j in neighbors(i, j, width, height):
                        if self.floor[n_j][n_i] != -1:
                            self.floor[n_j][n_i] += 1
                    self.floor[j][i] = -1
        if flashed:
            self.flash()

    def reset(self):
        height = len(self.floor)
        width = len(self.floor[0])
        self.last_flash_count = 0
        for j in range(0, height):
            for i in range(0, width):
                if self.floor[j][i] == -1:
                    self.floor[j][i] = 0
                    self.last_flash_count += 1
        self.flash_count += self.last_flash_count


def parse_input(input):
    rows = [line.strip() for line in input.split('\n') if line.strip()]
    floor = [[int(i) for i in r] for r in rows]
    return Ocean(floor)


def part1(input, steps):
    ocean = parse_input(input)
    for i in range(0, steps):
        ocean.step()
    return ocean.flash_count


def part2(input):
    ocean = parse_input(input)
    while ocean.last_flash_count != ocean.size:
        ocean.step()
    return ocean.step_count


if __name__ == '__main__':
    example = """
    5483143223
    2745854711
    5264556173
    6141336146
    6357385478
    4167524645
    2176841721
    6882881134
    4846848554
    5283751526
    """

    assert part1(example, 10) == 204
    assert part1(example, 100) == 1656
    with open('day11.in', 'r') as fh:
       input = fh.read()
    print(part1(input, 100))

    assert part2(example) == 195
    print(part2(input))
