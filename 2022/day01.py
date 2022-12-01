def parse(input):
    parsed = input.strip().split('\n')
    elves = []
    elf = []
    for calorie in parsed:
        if calorie == '':
            elves.append(elf)
            elf = []
        else:
            elf.append(int(calorie))
    elves.append(elf)
    return elves

def count_calories(elf_calories):
    return sum(elf_calories)

def part1(input):
    elves = parse(input)
    calories = [count_calories(i) for i in elves]
    return max(calories)

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
