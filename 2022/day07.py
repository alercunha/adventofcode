def parse(input):
    return [i.strip().split('\n') for i in input.split('$ ')]


def filter_dirs(current_dir, f):
    if f(current_dir):
        yield current_dir
    for k, v in current_dir.items():
        if k != '..' and isinstance(v, dict):
            for node in filter_dirs(v, f):
                yield node


def create_root(commands):
    root = {'..': None, '_size': 0}
    current_dir = root
    for command in commands:
        if not command[0]:
            continue
        if command[0].startswith('cd'):
            dir = command[0][3:]
            if dir == '..':
                current_dir = current_dir.get('..', root)
            elif dir == '/':
                current_dir = root
            else:
                current_dir[dir] = {'..': current_dir, '_size': 0}
                current_dir = current_dir[dir]
        elif command[0] == 'ls':
            for node in command[1:]:
                if node.startswith('dir'):
                    continue
                size_str, file = node.split(' ')
                size = int(size_str)
                current_dir[file] = size
                current_dir['_size'] += size
                parent = current_dir['..']
                while parent:
                    parent['_size'] += size
                    parent = parent['..']
    return root


def part1(commands):
    root = create_root(commands)
    def max_100k(node):
        return node['_size'] <= 100000
    return sum([d['_size'] for d in filter_dirs(root, max_100k)])


def part2(commands):
    root = create_root(commands)
    free_space = 70000000 - root['_size']
    delta = 30000000 - free_space
    def to_delete(node):
        return node['_size'] >= delta
    return min([d['_size'] for d in filter_dirs(root, to_delete)])


if __name__ == '__main__':
    example1 = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

    parsed_example1 = parse(example1)
    assert part1(parsed_example1) == 95437

    with open('day07.in', 'r') as fh:
        input = fh.read().strip()
    
    print(part1(parse(input)))

    assert part2(parsed_example1) == 24933642

    print(part2(parse(input)))
