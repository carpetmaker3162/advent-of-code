DAY = 6

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

    d=[(-1,0),(0,1),(1,0),(0,-1)]
    ii=cycle(d)
    with open(file) as f:
        for l in f.readlines():
            lines.append(list(l.strip()))
    for r,row in enumerate(lines):
        for c,cell in enumerate(row):
            if cell=='^':
                q=[(r,c)]
                dr,dc=next(ii)
                while q:
                    r,c=q.pop(0)
                    nr,nc=r+dr,c+dc
                    lines[r][c]='X'
                    while 0<=nr<len(lines) and 0<=nc<len(lines[0]) and lines[nr][nc]=='#':
                        dr,dc=next(ii)
                        nr,nc=r+dr,c+dc
                    if not(0<=nr<len(lines) and 0<=nc<len(lines[0])):
                        break
                    q.append((nr,nc))

    for l in lines: 
        ans+=l.count('X')
    return ans


def problem2(file):
    ans = 0
    lines = []

    d=[(-1,0),(0,1),(1,0),(0,-1)]

    with open(file) as f:
        for l in f.readlines():
            lines.append(list(l.strip()))
    for r,row in enumerate(lines):
        for c,cell in enumerate(row):
            if cell=='^':
                sr,sc=r,c
    def do():
        vis=set()
        ii=cycle(d)
        q=[(sr,sc)]
        dr,dc=next(ii)
        while q:
            r,c=q.pop(0)
            if (r,c,dr,dc) in vis:
                return True
            vis.add((r,c,dr,dc))
            nr,nc=r+dr,c+dc
            while 0<=nr<len(lines) and 0<=nc<len(lines[0]) and lines[nr][nc]=='#':
               dr,dc=next(ii)
               nr,nc=r+dr,c+dc
            if not(0<=nr<len(lines) and 0<=nc<len(lines[0])):
                return False
            q.append((nr,nc))
    loc=[]
    for r in range(len(lines)):
        for c in range(len(lines[0])):
            if lines[r][c]=='.':
                lines[r][c]='#'
                if do():
                    ans+=1
                    loc.append((r,c))
                lines[r][c]='.'
    return ans


if __name__ == '__main__':
    if 'debug' in sys.argv:
        print('PART 1:', problem1('input.txt'))
        print('PART 2:', problem2('input.txt'))
    else:
        print('PART 1:', problem1(f'input/{DAY}.in'))
        print('PART 2:', problem2(f'input/{DAY}.in'))
