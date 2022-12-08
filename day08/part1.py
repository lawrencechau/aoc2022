from __future__ import annotations
from collections import deque, Counter, defaultdict

import argparse
import os.path

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def traverse(a, x, y):

    # left
    for i in range(x):
        if a[i][y] >= a[x][y]:
            break
        if i == x-1:
            print(f'Tree {i}, {y}: {a[x][y]} is visible')
            return 1
    #right 
    for i in range(x+1,len(a)):
        if a[i][y] >= a[x][y]:
            break
        if i == len(a)-1:
            print(f'Tree {i}, {y}: {a[x][y]} is visible')
            return 1
    # top 
    for i in range(y):
        if a[x][i] >= a[x][y]:
            break
        if i == y-1:
            print(f'Tree {i}, {y}: {a[x][y]} is visible')
            return 1
    #right 
    for i in range(y+1,len(a[0])):
        if a[x][i] >= a[x][y]:
            break
        if i == len(a[0])-1:
            print(f'Tree {i}, {y}: {a[x][y]} is visible')
            return 1
    return 0


def compute(s: str) -> int:
    lines = s.splitlines()
    x,y = len(lines), len(lines[0])
    a = [[0 for _ in range(y)] for _  in range(x)]
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            a[i][j] = c

    ans = 0
    for i in range(x):
        for j in range(y):
            if i == 0 or i == (x-1) or j == 0 or j == (y-1):
                ans += 1
                continue
            ans += traverse(a, i, j)
            
    # TODO: implement solution here!
    return ans


INPUT_S = '''\
30373
25512
65332
33549
35390
'''
EXPECTED = 21


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
