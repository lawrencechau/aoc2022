advent of code 2022
===================

https://adventofcode.com/2022

## How to use

```sh
> virtualenv venv
> source venv/bin/activator

> cp -r day00 dayXX
> cd dayXX

# Download the input.txt
> aoc-download-input

# Start working in file
> vim input01.py
# Insert example in INPUT_S and set EXPECTED

# Run test
> pytest part1.py

# Submit
> python3 part1.py input.txt | aoc-submit --part 1

# Prep for part2 and do the same thing
> cp part1.py part2.py
```

## Bugs

```sh
~/git/aoc2022/day01$ python3 part1.py input.txt | aoc-submit --part
> 855 μs
Traceback (most recent call last):
  File "/home/***/git/aoc2022/venv/bin/aoc-submit", line 33, in <module>
    sys.exit(load_entry_point('support', 'console_scripts', 'aoc-submit')())
  File "/home/***/git/aoc2022/support/support.py", line 115, in submit_solution
    answer = int(sys.stdin.read())
ValueError: invalid literal for int() with base 10: '11223\n6323\n10725\n10761\n3587\n\n1274\n1041\n5566\n1759\n1372\n1619\n2228\n1283\n1981\n1885\n5894\n1321\n6081\n4407\n2992\n\n7184\n2310\n7975\n2752\n7942\n7616\n3622\n1320\n1231\n6191\n\n3069\n1069
```
