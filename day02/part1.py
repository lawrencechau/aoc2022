from __future__ import annotations

import argparse
import os.path

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    lines = s.splitlines()
    pts = 0
    for line in lines:
        a, b=line.split(' ')
        a = d[a]
        b = d[b]
        pt = p(int(a), int(b))
        print(f'{a} {b} => {pt}')
        pts += pt
        print
        pass
    return pts

d = { 
    'A': 1,
    'B' : 2,
    'C': 3,
    'X': 1,
    'Y': 2,
    'Z': 3,
}

# 0 = rock, b = paper, c = scissors

def p(a, b):
    if (b == 3 and a == 1):
        return b
    if (b > a) or (b == 1 and a == 3):
        return 6 + b
    elif (a == b):
        return 3 + b
    else:
        return b

INPUT_S = '''\
A Y
B X
C Z
'''
EXPECTED = 15


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
