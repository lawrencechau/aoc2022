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
        pt = p(a, b)
        print(f'{a} {b} => {pt}')
        pts += pt
        print
        pass
    return pts

d = { 
    'A': 1, #rock
    'B' : 2,#paper
    'C': 3,#scissorsjjj
}

# 
# X = lose, Y = draw, c = win 

def p(a, b):
    if b == 'X':
        return a-1 if a > 1 else 3 
    elif b == 'Y':
        return a + 3
    else:
        return (a+1 if a < 3 else 1) + 6


INPUT_S = '''\
A Y
B X
C Z
'''
EXPECTED = 12


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
