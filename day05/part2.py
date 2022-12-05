from __future__ import annotations

import argparse
import os.path

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

def rl(l):
    bl = l.split(' ')
    return (int(bl[1]) , int(bl[3]), int(bl[5]))

def mv(ss, c, ia, ib):
    print(c, ia, ib)
    ans = []
    for i in range(c):
        ans.append(ss[ia-1].pop())
    for a in ans[::-1]:
        ss[ib-1].append(a)

def compute(s: str) -> int:
    # read lines until reach number
    
    # get last number via index

    # read each line reversed (pushed on a stack)

    # push the numbers into the corresponding stack

    # command to parse line

    # execute command
    lines = s.splitlines()
    fl = False
    sl = []
    lc = 0
    ss = []
    for line in lines:
        if not line:
            print('0')
            continue 
        if not fl and '[' in line:
            print('1')
            sl.append(line)
        elif not fl and 'move' not in line:
            print('2')
            fl = True
            lc = int(line[-2])
            ss = [[] for _ in range(lc)] 
            print(f'lenght {lc}, ss {ss}')
            while sl:
                l = sl.pop()
                print(l)
                for i in range(lc):
                    ll = l[i * 4 + 1]
                    if not ll.isspace():
                        print(i-1, ll)
                        ss[i].append(ll)
            print(f'My arr{ss}')
        elif line[0]:
            # parse command
            print('3') 
            a, b, c = rl(line)
            mv(ss, a, b, c)
            print(f'My arr{ss}')
    print('Done')
    print(f'My arr{ss}')
    # TODO: implement solution here!
    return ''.join([sss[-1] for sss in ss])

INPUT_S = '''\
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
'''
EXPECTED = 'MCD'


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
