def gen1(factor, val, rounds):
    for _ in range(rounds):
        val = (val * factor) % 2147483647
        yield val


def part1(factorA, startA, factorB, startB, rounds):
    genA = gen1(factorA, startA, rounds)
    genB = gen1(factorB, startB, rounds)
    return sum(1 for a in genA if bin(a)[-16:] == bin(next(genB))[-16:])


def gen2(factor, val, mult, rounds):
    count = 0
    while count < rounds:
        val = (val * factor) % 2147483647
        if val % mult == 0:
            yield val
            count += 1


def part2(factorA, startA, multA, factorB, startB, multB, rounds):
    genA = gen2(factorA, startA, multA, rounds)
    genB = gen2(factorB, startB, multB, rounds)
    return sum(1 for a in genA if bin(a)[-16:] == bin(next(genB))[-16:])


if __name__ == '__main__':
    assert(part1(16807, 65, 48271, 8921, 5) == 1)
    print(part1(16807, 703, 48271, 516, 40*1000*1000))

    assert(part2(16807, 65, 4, 48271, 8921, 8, 1055) == 0)
    assert(part2(16807, 65, 4, 48271, 8921, 8, 1056) == 1)
    print(part2(16807, 703, 4, 48271, 516, 8, 5*1000*1000))
