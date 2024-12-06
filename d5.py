DAY = 5

import sys
import math
import re
from collections import *
from graphlib import TopologicalSorter as Topo

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

    r=defaultdict(list)
    for l in lines:
        if not l: continue
        if '|' in l:
            a,b=map(int,l.split('|'))
            r[b].append(a)
        else:
            page=list(map(int,l.split(',')))
            L=len(page)
            bad=False
            for i in range(L):
                for j in range(i+1,L):
                    if page[j] in r[page[i]]:
                        bad=True
                        break
            if not bad:
                ans+=page[L//2]

    return ans


def problem2(file):
    ans = 0
    lines = []

    with open(file) as f:
        for l in f.readlines():
            lines.append(l.strip())

    r=[]
    for l in lines:
        if not l: continue
        if '|' in l:
            a,b=map(int,l.split('|'))
            r.append((a,b))
    for l in lines:
        if ',' in l:
            update=list(map(int,l.split(',')))
            rnew=r[:]
            for a,b in r:
                if a not in update or b not in update:
                    rnew.remove((a,b))
            adj=defaultdict(list)
            for a,b in rnew:
                adj[a].append(b)
            master=list(Topo(adj).static_order())
            updatenew=sorted(update,key=lambda x: -master.index(x))
            if updatenew!=update:
                ans+=updatenew[len(update)//2]

    return ans


if __name__ == '__main__':
    if 'debug' in sys.argv:
        print('PART 1:', problem1('input.txt'))
        print('PART 2:', problem2('input.txt'))
    else:
        print('PART 1:', problem1(f'input/{DAY}.in'))
        print('PART 2:', problem2(f'input/{DAY}.in'))
