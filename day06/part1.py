from __future__ import annotations

import argparse
import os.path

import pytest
from collections import Counter

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    lines = s.splitlines()
    line = lines[0]
    for i in range(4, len(line)):
        a = line[i-4:i]
        if len(Counter(a)) == 4:
            return i
        pass
    # TODO: implement solution here!
    return -1


INPUT_S = '''\
nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg
'''
EXPECTED = 10


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (INPUT_S, EXPECTED),
        ('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 11),
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
