def parse(input):
    return [[int(x) for x in i] for i in input.split('\n')]


def tree_visible_left(trees, i, j):
    tree = trees[j][i]
    count = 0
    for x in range(i - 1, -1, -1):
        count += 1
        if trees[j][x] >= tree:
            return (False, count)
    return (True, count)


def tree_visible_right(trees, i, j):
    tree = trees[j][i]
    count = 0
    for x in range(i + 1, len(trees[0])):
        count += 1
        if trees[j][x] >= tree:
            return (False, count)
    return (True, count)


def tree_visible_top(trees, i, j):
    tree = trees[j][i]
    count = 0
    for x in range(j - 1, -1, -1):
        count += 1
        if trees[x][i] >= tree:
            return (False, count)
    return (True, count)


def tree_visible_bottom(trees, i, j):
    tree = trees[j][i]
    count = 0
    for x in range(j + 1, len(trees)):
        count += 1
        if trees[x][i] >= tree:
            return (False, count)
    return (True, count)


def tree_visible(trees, i, j):
    return \
        tree_visible_left(trees, i, j)[0] or \
        tree_visible_right(trees, i, j)[0] or \
        tree_visible_top(trees, i, j)[0] or \
        tree_visible_bottom(trees, i, j)[0]


def tree_visible_score(trees, i, j):
    return \
        tree_visible_left(trees, i, j)[1] * \
        tree_visible_right(trees, i, j)[1] * \
        tree_visible_top(trees, i, j)[1] * \
        tree_visible_bottom(trees, i, j)[1]


def part1(trees):
    sum = (len(trees) - 1) * 4
    for j in range(1, len(trees) - 1):
        for i in range(1, len(trees[0]) - 1):
            if tree_visible(trees, i, j):
                sum += 1
    return sum


def part2(trees):
    max_score = 0
    for i in range(len(trees[0])):
        for j in range(len(trees)):
            score = tree_visible_score(trees, i, j)
            max_score = max(score, max_score)
    return max_score


if __name__ == '__main__':
    example1 = """30373
25512
65332
33549
35390"""

    assert part1(parse(example1)) == 21

    with open('day08.in', 'r') as fh:
        input = fh.read().strip()
    
    print(part1(parse(input)))

    assert part2(parse(example1)) == 8

    print(part2(parse(input)))
