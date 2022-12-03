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

def f(a, b):
    b = {e: f for e, f in b}
    print(b)
    for c, d in a:
        if c in b:
            return c
    assert false


def compute(s: str) -> int:
    p = 0

    lines = s.splitlines()
    for line in lines:
        l = len(line)
        h = l//2
        l1, l2 = line[:h], line[h:]
        c1 = Counter(l1).most_common(l) 
        c2 = Counter(l2).most_common(l) 
        print(l1, l2)
        ch = f(c1, c2)
        #assert c1 == c2
        pt = pts(ch)
        print(f'{ch} => {pt}')
        p += pt
        pass
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
EXPECTED =157


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
