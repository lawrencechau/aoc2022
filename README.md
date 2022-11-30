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
