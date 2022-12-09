from __future__ import annotations
from collections import deque, Counter, defaultdict

import argparse
import os.path

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

# in range

# move

class Maze:
    def __init__(self):
        self.t = (0, 0)
        self.h = (0, 0)
        self.l = set()
        self.l.add((0, 0))

    def move_h(self, l, n):
        d = self.gd(l)
        dx, dy = d
        for _ in range(n):
            x, y = self.h
            self.h = (x+dx, y+dy)
            print(f'h {self.h}')
            self.move_t(l)

    def move_t(self,l):
        if self.t_in_range():
            return
        dx, dy = self.gd(l)
        dx, dy = dx * -1, dy * -1
        x, y = self.h
        self.t = (x+dx, y+dy)
        print(f't {self.t}')
        self.l.add(self.t)

    def t_in_range(self):
        d = [(0,0), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
        for dd in d:
            dx, dy = dd
            x, y = self.t
            dt = (x+dx, y+dy)
            if self.h == dt:
                return True
        return False
        

    def gd(self, l):
        if (l == 'R'):
            return (1, 0)
        elif (l == 'D'):
            return (0, -1)
        elif (l == 'L'):
            return (-1, 0)
        else:
            return (0, 1)

    def print(self):
        mx, my = 0, 0
        for x, y in self.l:
            mx = max(mx, x)
            my = max(my, y)

        for i in range(mx, -1, -1):
            s = ''
            for j in range(my):
                if (i, j) == (0, 0):
                    s += 's'
                elif (i,j) in self.l:
                    s += '#'
                else:
                    s+='.'
            print(s)



def compute(s: str) -> int:
    lines = s.splitlines()
    m = Maze()
    for line in lines:
        print(line)
        ls = line.split()
        d, n = ls[0], int(ls[1])
        m.move_h(d, n)
        pass
    # TODO: implement solution here!
    m.print()
    print(m.l)
    return len(m.l)


INPUT_S = '''\
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
'''
EXPECTED = 13


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
