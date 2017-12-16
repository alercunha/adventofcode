import re


def process(input):
    ops = {
        'inc': lambda x, y: x + y,
        'dec': lambda x, y: x - y,
    }
    comps = {
        '>': lambda x, y: x > y,
        '<': lambda x, y: x < y,
        '>=': lambda x, y: x >= y,
        '<=': lambda x, y: x <= y,
        '==': lambda x, y: x == y,
        '!=': lambda x, y: x != y,
    }
    lines = [l.strip() for l in input.split('\n') if l.strip()]
    pattern = '(\w+) (inc|dec) (-?\d+) if (\w+) ([><!=]=?) (-?\d+)'
    regs = {}
    high = 0
    for l in lines:
        match = re.search(pattern, l)
        if not match:
            raise Exception('Invalid input line: {0}'.format(l))
        reg1, op, val1, reg2, comp, val2 = match.groups()
        if comps[comp](regs.get(reg2, 0), int(val2)):
            regs[reg1] = ops[op](regs.get(reg1, 0), int(val1))
            high = max(high, regs[reg1])
    return max(regs.values()), high


def part1(input):
    return process(input)[0]


def part2(input):
    return process(input)[1]


if __name__ == '__main__':
    a = """
    b inc 5 if a > 1
    a inc 1 if b < 5
    c dec -10 if a >= 1
    c inc -20 if c == 10
    """
    assert(part1(a) == 1)

    with open('day8.in', 'r') as fh:
        data = fh.read()
    print(part1(data))

    assert(part2(a) == 10)
    print(part2(data))

