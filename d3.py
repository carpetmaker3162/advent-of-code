DAY = 3

import sys
import math
import re

def pr(x, *args, **kwargs):
    print(x, *args, **kwargs)
    return x

def uints(string, indexes=False):
    if indexes:
        nums = re.finditer(r'\d+', string)
        return [(x.start(), int(string[x.start():x.end()])) for x in nums]
    else:
        nums = re.findall(r'\d+', string)
        return [*map(int, nums)]

def ints(string, indexes=False):
    if indexes:
        nums = re.finditer(r'-?\d+', string)
        return [(x.start(), int(string[x.start():x.end()])) for x in nums]
    else:
        nums = re.findall(r'-?\d+', string)
        return [*map(int, nums)]


def problem1(file):
    ans = 0
    lines = []

    #with open(file) as f:
    #    for l in f.readlines():
    #        lines.append(l.strip())
    with open(file) as f:
        f=f.read()
    for x,y in re.findall('mul\((\d+),(\d+)\)', f):
        x=int(x)
        y=int(y)
        ans+=x*y

    return ans


def problem2(file):
    ans = 0
    lines = []

    #with open(file) as f:
    #    for l in f.readlines():
    #        lines.append(l.strip())
    with open(file) as f:
        f=f.read()
    enabled=True
    for m in re.findall('(mul\((\d+),(\d+)\)|don\'t\(\)|do\(\))', f):
        if m[0]=='do()':
            enabled=True
        elif m[0]=='don\'t()':
            enabled=False
        else:
            if enabled: ans+=int(m[1])*int(m[2])

    return ans


if __name__ == '__main__':
    if 'debug' in sys.argv:
        print('PART 1:', problem1('input.txt'))
        print('PART 2:', problem2('input.txt'))
    else:
        print('PART 1:', problem1(f'input/{DAY}.in'))
        print('PART 2:', problem2(f'input/{DAY}.in'))
