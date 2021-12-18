from functools import reduce


def parse_input(input):
    return [
        [
            part.strip().split()
            for part in line.strip().split('|')
        ]
        for line in input.split('\n') if line.strip()
    ]


def part1(input):
    data = parse_input(input)
    return sum([sum(1 for o in output if len(o) in [2, 3, 4, 7]) for _, output in data])


def part2(input):
    data = parse_input(input)
    total = 0
    for row in data:
        digits = row[0] + row[1]
        digits = set([''.join(sorted(d)) for d in digits])
        digits = sorted(digits, key=lambda i: len(i))
        one, seven, four = digits[:3]
        eight = digits[-1]
        digits = digits[3:-1]
        nine = [d for d in digits if len(d) == 6 and all(i in d for i in four)][0]
        zero = [d for d in digits if len(d) == 6 and d != nine and all(i in d for i in one)][0]
        six = [d for d in digits if len(d) == 6 and d != nine and d != zero][0]
        three = [d for d in digits if len(d) == 5 and all(i in d for i in one)][0]
        five = [d for d in digits if len(d) == 5 and d != three and sum(1 for i in four if i in d) == 3][0]
        two = [d for d in digits if len(d) == 5 and d != three and d != five][0]
        map = {
            one: '1', two: '2', three: '3', four: '4', five: '5', six: '6', seven: '7', eight: '8', nine: '9', zero: '0'
        }
        out_digits = [''.join(sorted(d)) for d in row[1]]
        output = ''.join([map[i] for i in out_digits])
        total += int(output)

    return total


if __name__ == '__main__':
    example = """
    be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
    edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
    fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
    fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
    aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
    fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
    dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
    bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
    egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
    gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
    """

    assert part1(example) == 26
    with open('day08.in', 'r') as fh:
       input = fh.read()
    print(part1(input))

    assert part2(example) == 61229
    print(part2(input))
