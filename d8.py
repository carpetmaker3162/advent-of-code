DAY = 8

import sys
import math
import re
from collections import *
from itertools import *

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

    with open(file) as f:
        for l in f.readlines():
            lines.append(l.strip())
    R=len(lines)
    C=len(lines[0])
    antinode=[[0 for i in range(C)] for i in range(R)]
    antennas=defaultdict(list)
    for r,row in enumerate(lines):
        for c,cell in enumerate(row):
            if cell!='.':
                antennas[cell].append((r,c))
    for a,ls in antennas.items():
        for r1,c1 in ls:
            for r2,c2 in ls:
                if r1==r2 and c1==c2: continue
                dr,dc=r2-r1,c2-c1
                nr1,nc1=r1-dr,c1-dc
                nr2,nc2=r2+dr,c2+dc
                if 0<=nr1<R and 0<=nc1<C:
                    antinode[nr1][nc1]=1
                if 0<=nr2<R and 0<=nc2<C:
                    antinode[nr2][nc2]=1
    for a in antinode:
        ans+=sum(a)

    return ans


def problem2(file):
    ans = 0
    lines = []

    with open(file) as f:
        for l in f.readlines():
            lines.append(l.strip())
    R=len(lines)
    C=len(lines[0])
    antinode=[[0 for i in range(C)] for i in range(R)]
    antennas=defaultdict(list)
    for r,row in enumerate(lines):
        for c,cell in enumerate(row):
            if cell!='.':
                antennas[cell].append((r,c))
    for a,ls in antennas.items():
        for r1,c1 in ls:
            for r2,c2 in ls:
                if r1==r2 and c1==c2: continue
                dr,dc=r2-r1,c2-c1
                d=0
                nr1,nc1=r1-dr*d,c1-dc*d
                while 0<=nr1<R and 0<=nc1<C:
                    antinode[nr1][nc1]=1
                    d+=1
                    nr1,nc1=r1-dr*d,c1-dc*d
                d=0
                nr2,nc2=r2+dr*d,c2+dc*d
                while 0<=nr2<R and 0<=nc2<C:
                    antinode[nr2][nc2]=1
                    d+=1
                    nr2,nc2=r2+dr*d,c2+dc*d
    for a in antinode:
        ans+=sum(a)

    return ans


if __name__ == '__main__':
    if 'debug' in sys.argv:
        print('PART 1:', problem1('input.txt'))
        print('PART 2:', problem2('input.txt'))
    else:
        print('PART 1:', problem1(f'input/{DAY}.in'))
        print('PART 2:', problem2(f'input/{DAY}.in'))
