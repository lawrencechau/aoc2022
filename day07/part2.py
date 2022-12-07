from __future__ import annotations
from collections import deque, Counter, defaultdict

import argparse
import os.path

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

class F:
    def __init__(self, n, p):
        self.n = n
        self.c = {}
        self.p = p
        self.size = 0

def compute(s: str) -> int:
    lines = s.splitlines()
    root = F('/', None)
    curr = root
    for line in lines:
        print(line)
        if line[0] == '$':
            l = line.split(' ')
            cmd = l[1]
            if cmd == 'cd':
                n = l[2]
                if n == '..':
                    curr = curr.p
                elif n == '/':
                    curr = root
                else:
                    if n not in curr.c:
                        curr.c[n] = F(n, curr)
                    curr = curr.c[n]
                print(curr)
            else:
                continue
        else:
            l = line.split(' ')
            if l[0] == 'dir':
                n = l[1]
                if n not in curr.c:
                    curr.c[n] = F(n, curr)
            else:
                fs = int(l[0])
                z = curr
                while z:
                    z.size += fs
                    print(f'{z.n}: {z.size}')
                    z = z.p

    print('Calculating')
    ans = []
    q = [root]
    while q:
        cf = q.pop()
        print(f'{cf.n}')
        for ch in cf.c.values():
            q.append(ch)
        ans.append(cf.size)

    t = 30000000 - (70000000 - root.size)
    print(f'Target: {t}')
    print('smallest delete')
    ans.sort()
    print(ans)
    sans = root.size
    print(len(ans))
    for i in range(len(ans)):
        sans = ans[i]
        print(f'curr {sans}')
        if sans > t:
            break
    
    return sans


INPUT_S = '''\
$ cd /
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
7214296 k
'''
EXPECTED = 24933642


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (INPUT_S, EXPECTED),
    ),
)
def test(input_s: str, expected: int) -> None:
    assert compute(input_s) == expected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f, support.timing():
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
