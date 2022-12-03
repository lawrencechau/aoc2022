from __future__ import annotations

import argparse
import os.path
from collections import Counter

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def pts(a):
    # captial
    if a < 'a':
        return ord(a) - ord('A') + 27
    else:
        return ord(a) - ord('a') + 1

def f(a, b, g):
    b = {e: f for e, f in b}
    g = {h: i for h, i in g}
    print(b)
    for c, d in a:
        if c in b and c in g:
            return c
    assert false

def gl(ln):
    l = len(ln)
    h = l//2
    c1 = Counter(ln).most_common(l) 
    return c1

def compute(s: str) -> int:
    p = 0

    lines = s.splitlines()
    i = 0
    while (i < len(lines)):
        l1, l2, l3 = gl(lines[i]), gl(lines[i+1]), gl(lines[i+2])
        ch = f(l1, l2, l3)
        #assert c1 == c2
        pt = pts(ch)
        print(f'{ch} => {pt}')
        p += pt
        i += 3

    # TODO: implement solution here!
    return p


INPUT_S = '''\
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
'''
EXPECTED =70


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
