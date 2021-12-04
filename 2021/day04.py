class Board:
    def __init__(self):
        self.matrix = [[None] * 5 for _ in range(5)]
        self.won = False

    def set_value(self, x, y, num):
        self.matrix[y][x] = num

    def pop(self, x, y):
        if self.won:
            return False
        self.matrix[y][x] = None
        self.won = all(i is None for i in self.line(y)) or all(i is None for i in self.row(x))
        return self.won

    def line(self, y):
        for i in range(5):
            yield self.matrix[y][i]

    def row(self, x):
        for i in range(5):
            yield self.matrix[i][x]

    def iterate(self):
        for x in range(5):
            for y in range(5):
                yield self.matrix[y][x]

    def sum_unmarked(self):
        return sum([i or 0 for i in self.iterate()])


def read_board(rows, board_idx, draw_map):
    board = Board()
    for y, row in enumerate(rows):
        for x, num in enumerate([int(num) for num in row.split()]):
            board.set_value(x, y, num)
            positions = draw_map.get(num, None)
            if not positions:
                positions = list()
                draw_map[num] = positions
            positions.append((board_idx, x, y))
    return board


def parse_input(input):
    rows = [r.strip() for r in input.split('\n') if r.strip()]
    draws = [int(num) for num in rows[0].split(',')]

    draw_map = {}
    boards = list()
    rows = rows[1:]
    while len(rows) > 0:
        board = read_board(rows[0:5], len(boards), draw_map)
        rows = rows[5:]
        boards.append(board)

    return draws, boards, draw_map


def draw(draws, boards, draw_map):
    while len(draws) > 0:
        num = draws.pop(0)
        found = None
        for board_idx, x, y in draw_map[num]:
            board = boards[board_idx]
            if board.pop(x, y):
                found = board
        if found:
            return found.sum_unmarked() * num
    return None


def part1(input):
    draws, boards, draw_map = parse_input(input)
    return draw(draws, boards, draw_map)


def part2(input):
    draws, boards, draw_map = parse_input(input)
    score = draw(draws, boards, draw_map)
    last = None
    while score is not None:
        last = score
        score = draw(draws, boards, draw_map)
    return last


if __name__ == '__main__':
    example = """
    7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

    22 13 17 11  0
     8  2 23  4 24
    21  9 14 16  7
     6 10  3 18  5
     1 12 20 15 19
    
     3 15  0  2 22
     9 18 13 17  5
    19  8  7 25 23
    20 11 10 24  4
    14 21 16 12  6
    
    14 21 17 24  4
    10 16 15  9 19
    18  8 23 26 20
    22 11 13  6  5
     2  0 12  3  7
    """
    assert part1(example) == 4512
    with open('day04.in', 'r') as fh:
        input = fh.read()
    print(part1(input))

    assert part2(example) == 1924
    print(part2(input))
