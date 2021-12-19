def parse_input(input):
    return [line.strip() for line in input.split('\n') if line.strip()]


openings = {
    '}': '{',
    ')': '(',
    ']': '[',
    '>': '<',
}

closings = {v: k for k, v in openings.items()}

illegal_points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

autocomplete_points = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}


def process(row, stack):
    if len(row) == 0:
        return None
    r = row.pop(0)
    if r not in openings:
        stack.append(r)
    else:
        c = openings[r]
        if stack[-1] == c:
            stack.pop(-1)
        else:
            return r
    return process(row, stack)


def find_illegal(row):
    stack = list()
    r = process(list(row), stack)
    return illegal_points[r] if r else 0


def find_closing(row):
    stack = list()
    r = process(list(row), stack)
    if not r:
        return [closings[o] for o in reversed(stack)]
    else:
        return []


def part1(input):
    data = parse_input(input)
    return sum(find_illegal(r) for r in data)


def autocomplete_score(closings):
    total = 0
    for c in closings:
        points = autocomplete_points[c]
        total = total * 5 + points
    return total


def part2(input):
    data = parse_input(input)
    scores = [autocomplete_score(find_closing(row)) for row in data]
    scores = sorted([s for s in scores if s != 0])
    return scores[int(len(scores)/2)]


if __name__ == '__main__':
    example = """
    [({(<(())[]>[[{[]{<()<>>
    [(()[<>])]({[<{<<[]>>(
    {([(<{}[<>[]}>{[]{[(<()>
    (((({<>}<{<{<>}{[]{[]{}
    [[<[([]))<([[{}[[()]]]
    [{[{({}]{}}([{[{{{}}([]
    {<[[]]>}<{[{[{[]{()[[[]
    [<(<(<(<{}))><([]([]()
    <{([([[(<>()){}]>(<<{{
    <{([{{}}[<[[[<>{}]]]>[]]
    """

    assert part1(example) == 26397
    with open('day10.in', 'r') as fh:
       input = fh.read()
    print(part1(input))

    assert part2(example) == 288957
    print(part2(input))
