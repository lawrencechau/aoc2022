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
        self.t = [(0,0) for _ in range(10)]
        self.l = set()
        self.l.add((0, 0))

    def move_h(self, l, n):
        d = self.gd(l)
        dx, dy = d
        for _ in range(n):
            x, y = self.t[0]
            self.t[0] = (x+dx, y+dy)
            for idx in range(1, 10):
                self.move_t(l, idx)
            print(self.t)

    def move_t(self,l, idx):
        if self.t_in_range(idx):
            return
        # x or y
        hx, hy = self.t[idx-1][0], self.t[idx-1][1]
        tx, ty = self.t[idx][0], self.t[idx][1]
        dx, dy = 0, 0
        if hx == tx:
            if hy > ty:
                dy = 1
            else:
                dy = -1
        elif hy == ty:
            if hx > tx:
                dx = 1
            else:
                dx = -1
        else:
            if hx > tx:
                dx = 1
            else:
                dx = -1
            if hy > ty:
                dy = 1
            else:
                dy = -1

        self.t[idx] = (tx+dx, ty+dy)
        print(f'{idx} {self.t[idx]}')
        if idx == 9:
            self.l.add(self.t[idx])

    def t_in_range(self, idx):
        d = [(0,0), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
        for dd in d:
            dx, dy = dd
            x, y = self.t[idx]
            dt = (x+dx, y+dy)
            if self.t[idx-1] == dt:
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
    # m.print()
    # print(m.l)
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
EXPECTED = 1

INPUT_S2 = '''\
R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
'''
EXPECTED2 = 36


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (INPUT_S, EXPECTED),
        (INPUT_S2, EXPECTED2),
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
