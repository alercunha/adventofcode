def parse(input):
    parsed = [i.split('\n') for i in input.strip().split('\n\n')]
    return [list(map(int, i)) for i in parsed]

def count_calories(elf_calories):
    return sum(elf_calories)

def part1(input):
    elves = parse(input)
    calories = [count_calories(i) for i in elves]
    return max(calories)

def part2(input):
    elves = parse(input)
    calories = [count_calories(i) for i in elves]
    calories.sort()
    return sum(calories[-3:])

if __name__ == '__main__':
    example1 = """
    1000
    2000
    3000

    4000

    5000
    6000

    7000
    8000
    9000

    10000
    """
    
    assert parse(example1) == [[1000,2000,3000],[4000],[5000,6000],[7000,8000,9000],[10000]]

    assert count_calories(parse(example1)[0]) == 6000

    assert part1(example1) == 24000

    print(part1(example1))

    with open('day01.in', 'r') as fh:
        input = fh.read()

    print(part1(input))

    assert part2(example1) == 45000

    print(part2(input))
