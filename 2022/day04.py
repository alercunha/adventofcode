def parse(input):
    parsed = [
        [j.split('-') for j in i.strip().split(',')] 
        for i in input.strip().split('\n')
    ]
    return [[list(map(int, i)) for i in j] for j in parsed]


def part1(input):
    sum = 0
    for assign in input:
        if assign[0][0] <= assign[1][0] and assign[0][1] >= assign[1][1]:
            sum +=1
        elif assign[0][0] >= assign[1][0] and assign[0][1] <= assign[1][1]:
            sum +=1
    return sum


def part2(input):
    sum = 0
    for assign in input:
        if assign[0][0] < assign[1][0]:
            if assign[0][1] >= assign[1][0]:
                sum += 1
        elif assign[1][1] >= assign[0][0]:
            sum += 1
    return sum


if __name__ == '__main__':
    example1 = """
    2-4,6-8
    2-3,4-5
    5-7,7-9
    2-8,3-7
    6-6,4-6
    2-6,4-8
    """

    parsed_example1 = parse(example1)
    assert parsed_example1[0] == [[2,4],[6,8]]
    assert parsed_example1[1] == [[2,3],[4,5]]

    assert part1(parsed_example1) == 2

    with open('day04.in', 'r') as fh:
        input = fh.read()
    
    print(part1(parse(input)))

    assert part2(parsed_example1) == 4

    print(part2(parse(input)))
