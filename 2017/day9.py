def traverse(input, garbage=[]):
    stack = list()
    score = 0
    for pos in range(len(input)):
        c = input[pos]
        if len(stack) > 0 and (stack[-1] == '<' or stack[-1] == '!'):  # trashing
            if c == '>' or stack[-1] == '!':
                stack.pop()
            elif c == '!':
                stack.append(c)
            else:
                garbage.append(c)
        else:
            if c == '{' or c == '<' or c == '!':
                stack.append(c)
                if c == '{':
                    score += 1
            elif c == '}':
                stack.pop()
                yield score
                score -= 1


def part1(input):
    return sum(traverse(input))


def part2(input):
    garbage = []
    list(traverse(input, garbage))
    return len(garbage)


if __name__ == '__main__':
    assert(part1('{}') == 1)
    assert(part1('{{{}}}') == 6)
    assert(part1('{{},{}}') == 5)
    assert(part1('{{{},{},{{}}}}') == 16)
    assert(part1('{<a>,<a>,<a>,<a>}') == 1)
    assert(part1('{{<ab>},{<ab>},{<ab>},{<ab>}}') == 9)
    assert(part1('{{<!!>},{<!!>},{<!!>},{<!!>}}') == 9)
    assert(part1('{{<a!>},{<a!>},{<a!>},{<ab>}}') == 3)

    with open('day9.in', 'r') as fh:
        data = fh.read().strip()
    print(part1(data))

    assert(part2('<>') == 0)
    assert(part2('<random characters>') == 17)
    assert(part2('<<<<>') == 3)
    assert(part2('<{!>}>') == 2)
    assert(part2('<!!>') == 0)
    assert(part2('<!!!>>') == 0)
    assert(part2('<{o"i!a,<{i<a>') == 10)
    print(part2(data))
