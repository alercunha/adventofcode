def parse(input):
    lines = [l.strip() for l in input.split('\n') if l.strip()]
    return {
        i[0]: i[1] for i in
        ([int(i.strip()) for i in l.split(':')] for l in lines)
    }


def run(fw, delay=0):
    for ix in fw.keys():
        if (ix + delay) > 0 and (ix + delay) % ((fw[ix] - 1) * 2) == 0:
            yield ix * fw[ix]


def part1(input):
    return sum(run(parse(input)))


def part2(input):
    fw = parse(input)
    ix = 0
    while True:
        if not any((True for _ in run(fw, ix))):
            return ix
        ix += 1


if __name__ == '__main__':
    a = '''
    0: 3
    1: 2
    4: 4
    6: 4
    '''
    assert(part1(a) == 24)

    with open('day13.in', 'r') as fh:
        data = fh.read().strip()
    print(part1(data))

    assert(part2(a) == 10)
    print(part2(data))
