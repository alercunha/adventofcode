def parse(input):
    groups = [i.split('\n') for i in input.split('\n\n')]
    monkeys = []
    for group in groups:
        monkey = {
            'items': [int(s.strip()) for s in group[1][17:].split(',')],
            'op': group[2][18:].strip(),
            'test': int(group[3][20:].strip()),
            'test_true': int(group[4][28:].strip()),
            'test_false': int(group[5][29:].strip()),
            'inspect_count': 0
        }
        monkeys.append(monkey)
    return monkeys


op_map = {
    '*': lambda x, y: x * y,
    '+': lambda x, y: x + y,
}


def run_op(worry, op):
    op = op.replace('old', str(worry))
    args = op.split()
    f = op_map[args[1]]
    return f(int(args[0]), int(args[2]))


def run_rounds(monkeys, rounds, cap_func):
    for _ in range(rounds):
        for monkey in monkeys:
            while len(monkey['items']) > 0:
                monkey['inspect_count'] += 1
                worry = monkey['items'].pop(0)
                worry = run_op(worry, monkey['op'])
                worry = cap_func(worry)
                throw_to = monkey['test_true'] if worry % monkey['test'] == 0 else monkey['test_false']
                monkeys[throw_to]['items'].append(worry)


def part1(monkeys):
    def cap_func(worry):
        return int(worry / 3)
    
    run_rounds(monkeys, 20, cap_func)
    top = sorted([m['inspect_count'] for m in monkeys])
    return top[-1] * top[-2]


def part2(monkeys):
    max = 1
    for m in monkeys:
        max *= m['test']
    def cap_func(worry):
        return worry % max
    
    run_rounds(monkeys, 10000, cap_func)
    top = sorted([m['inspect_count'] for m in monkeys])
    return top[-1] * top[-2]


if __name__ == '__main__':
    example1 = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""

    assert part1(parse(example1)) == 10605

    with open('day11.in', 'r') as fh:
        input = fh.read().strip()
    
    print(part1(parse(input)))

    assert part2(parse(example1)) == 2713310158

    print(part2(parse(input)))
