def parse(input):
    return [list(i.strip()) for i in input.strip().split('\n')]


def find_shared_item(rucksack):
    half = int(len(rucksack) / 2)
    for i in range(0, half):
        if rucksack[i] in rucksack[half :]:
            return rucksack[i]


def get_priority(item):
    return 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'.index(item) + 1


def part1(input):
    sum = 0
    for rucksack in input:
        shared_item = find_shared_item(rucksack)
        sum += get_priority(shared_item)
    return sum


def find_badge(input, group):
    first = input[group]
    for i in list(first):
        if i in input[group + 1] and i in input[group + 2]:
            return i


def part2(input):
    sum = 0
    for i in range(0, int(len(input) / 3)):
        badge = find_badge(input, i * 3)
        sum += get_priority(badge)
    return sum


if __name__ == '__main__':
    example1 = """
    vJrwpWtwJgWrhcsFMMfFFhFp
    jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
    PmmdzqPrVvPwwTWBwg
    wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
    ttgJtRGJQctTZtZT
    CrZsJsPPZsGzwwsLwLmpwMDw
    """
    parsed_example1 = parse(example1)
    assert parsed_example1[0] == list('vJrwpWtwJgWrhcsFMMfFFhFp')
    assert parsed_example1[1] == list('jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL')

    assert part1(parse(example1)) == 157

    with open('day03.in', 'r') as fh:
        input = fh.read()
    
    print(part1(parse(input)))

    assert part2(parse(example1)) == 70

    print(part2(parse(input)))
