def parse(input):
    return [i.split() for i in input.split('\n')]


def run_instructions(instructions):
    x = 1
    cycles = []
    for instruction in instructions:
        if instruction[0] == 'noop':
            cycles.append(x)
        elif instruction[0] == 'addx':
            cycles.append(x)
            cycles.append(x)
            x += int(instruction[1])
    return cycles


def part1(instructions):
    cycles = run_instructions(instructions)
    strength_cycles = [20, 60, 100, 140, 180, 220]
    return sum([cycles[s - 1] * s for s in strength_cycles])


def part2(instructions):
    cycles = run_instructions(instructions)
    pixels = [['.' for _ in range(40)] for _ in range(6)]
    for j in range(6):
        for i in range(40):
            position = j * 40 + i
            if i >= cycles[position] -1 and i <= cycles[position] + 1:
                pixels[j][i] = '#'
    return pixels

if __name__ == '__main__':
    example1 = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""

    assert part1(parse(example1)) == 13140

    with open('day10.in', 'r') as fh:
        input = fh.read().strip()
    
    print(part1(parse(input)))

    pixels = part2(parse(example1))
    assert ''.join(pixels[0]) == '##..##..##..##..##..##..##..##..##..##..'
    assert ''.join(pixels[1]) == '###...###...###...###...###...###...###.'
    assert ''.join(pixels[2]) == '####....####....####....####....####....'
    assert ''.join(pixels[3]) == '#####.....#####.....#####.....#####.....'
    assert ''.join(pixels[4]) == '######......######......######......####'
    assert ''.join(pixels[5]) == '#######.......#######.......#######.....'

    pixels = part2(parse(input))
    for row in pixels:
        print(''.join(row))
