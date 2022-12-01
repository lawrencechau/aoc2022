from __future__ import annotations

import heapq
import argparse
import os.path

import pytest
import sys

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    # numbers = support.parse_numbers_split(s)
    # for n in numbers:
    #     pass

    lines = s.splitlines()
    ans = 0
    tmp = 0
    h = []
    for line in lines:
        try:
            tmp += int(line)
        except Exception:
            heapq.heappush(h, tmp)
            tmp = 0
        print(line)
        pass
    heapq.heappush(h, tmp)
    print(h)
    thre = heapq.nlargest(3, h)
    print(thre)
    ans = sum(thre)
    return ans


INPUT_S = '''\
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
'''
EXPECTED = 55000


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
