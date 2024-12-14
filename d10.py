DAY = 10

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

d=[(0,1),(1,0),(-1,0),(0,-1)]
def problem1(file):
    ans = 0
    lines = []

    with open(file) as f:
        for l in f.readlines():
            lines.append(list(map(int,l.strip())))

    R=len(lines)
    C=len(lines[0])
    for rr,row in enumerate(lines):
        for cc,cell in enumerate(row):
            if cell==0:
                q=[(rr,cc)]
                loc=set()
                while q:
                    r,c=q.pop(0)
                    if lines[r][c]==9:
                        loc.add((r,c))
                    for dr,dc in d:
                        nr,nc=r+dr,c+dc
                        if 0<=nr<R and 0<=nc<C and lines[nr][nc]==lines[r][c]+1:
                            q.append((nr,nc))
                ans+=len(loc)
    return ans


def problem2(file):
    ans = 0
    lines = []

    with open(file) as f:
        for l in f.readlines():
            lines.append(list(map(int,l.strip())))

    R=len(lines)
    C=len(lines[0])
    for rr,row in enumerate(lines):
        for cc,cell in enumerate(row):
            if cell==0:
                q=[(rr,cc)]
                while q:
                    r,c=q.pop(0)
                    if lines[r][c]==9:
                        ans+=1
                    for dr,dc in d:
                        nr,nc=r+dr,c+dc
                        if 0<=nr<R and 0<=nc<C and lines[nr][nc]==lines[r][c]+1:
                            q.append((nr,nc))
    return ans


if __name__ == '__main__':
    if 'debug' in sys.argv:
        print('PART 1:', problem1('input.txt'))
        print('PART 2:', problem2('input.txt'))
    else:
        print('PART 1:', problem1(f'input/{DAY}.in'))
        print('PART 2:', problem2(f'input/{DAY}.in'))
