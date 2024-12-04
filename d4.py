DAY = 4

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

    with open(file) as f:
        for l in f.readlines():
            lines.append(l.strip())

    s='XMAS'
    R=len(lines)
    C=len(lines[0])
    d=[(1,1),(1,-1),(-1,1),(-1,-1),(0,1),(1,0),(-1,0),(0,-1)]
    for r in range(R):
        for c in range(C):
            if lines[r][c]!='X':
                continue
            for dr,dc in d:
                for dd in range(1,4):
                    nr,nc=r+dr*dd,c+dc*dd
                    if 0<=nr<R and 0<=nc<C:
                        if lines[nr][nc]!=s[dd]:
                            break
                    else:
                        break
                else:
                    ans+=1

    return ans


def problem2(file):
    ans = 0
    lines = []

    with open(file) as f:
        for l in f.readlines():
            lines.append(l.strip())

    R=len(lines)
    C=len(lines[0])
    tgts=['M.S.A.M.S','M.M.A.S.S','S.S.A.M.M','S.M.A.S.M']
    for r in range(R-2):
        for c in range(C-2):
            sq=lines[r][c:c+3]+lines[r+1][c:c+3]+lines[r+2][c:c+3]
            for poss in tgts:
                for i in range(len(poss)):
                    if poss[i]=='.':
                        continue
                    if poss[i]!=sq[i]:
                        break
                else:
                    ans+=1
                    continue

    return ans


if __name__ == '__main__':
    if 'debug' in sys.argv:
        print('PART 1:', problem1('input.txt'))
        print('PART 2:', problem2('input.txt'))
    else:
        print('PART 1:', problem1(f'input/{DAY}.in'))
        print('PART 2:', problem2(f'input/{DAY}.in'))
