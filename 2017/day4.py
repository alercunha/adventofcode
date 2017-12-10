def uniques(line):
    words = sorted(line.split(' '))
    for i in range(len(words) - 1):
        if words[i] == words[i + 1]:
            return False
    return True


def part1(input):
    lines = [l.strip() for l in input.split('\n') if l.strip()]
    return sum(1 for l in lines if uniques(l))


def has_anagram(line):
    words = sorted(''.join(sorted(w)) for w in line.split(' '))
    for i in range(len(words) - 1):
        if words[i] == words[i + 1]:
            return True
    return False


def part2(input):
    lines = [l.strip() for l in input.split('\n') if l.strip()]
    return sum(1 for l in lines if not has_anagram(l))


if __name__ == '__main__':
    a = [
        'aa bb cc dd ee',
        'aa bb cc dd aa',
        'aa bb cc dd aaa'
    ]
    assert([uniques(i) for i in a] == [True, False, True])
    assert(part1('\n'.join(a)) == 2)
    with open('day4.in', 'r') as fh:
        day4_input = fh.read()
    print(part1(day4_input))

    b = [
        'abcde fghij',
        'abcde xyz ecdab',
        'a ab abc abd abf abj',
        'iiii oiii ooii oooi oooo',
        'oiii ioii iioi iiio'
    ]
    assert([has_anagram(i) for i in b] == [False, True, False, False, True])
    print(part2(day4_input))
