DAY = 7

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
    def op(x,y,i):
        if state&i:
            return x+y
        else:
            return x*y
    for l in lines:
        l=ints(l)
        tg=l[0]
        v=l[1:]
        for state in range(2**(len(v)-1)):
            temp=v[0]
            for i in range(1,len(v)):
                temp=op(temp,v[i],2**(i-1))
            if temp==tg:
                ans+=tg
                break

    return ans


def problem2(file):
    ans = 0
    lines = []

    with open(file) as f:
        for l in f.readlines():
            lines.append(l.strip())
    def op(x,y,i):
        if state//i%3==0:
            return x+y
        elif state//i%3==1:
            return int(str(x)+str(y))
        else:
            return x*y
    for l in lines:
        l=ints(l)
        tg=l[0]
        v=l[1:]
        for state in range(3**(len(v)-1)):
            temp=v[0]
            for i in range(1,len(v)):
                temp=op(temp,v[i],3**(i-1))
            if temp==tg:
                ans+=tg
                break

    return ans


if __name__ == '__main__':
    if 'debug' in sys.argv:
        print('PART 1:', problem1('input.txt'))
        print('PART 2:', problem2('input.txt'))
    else:
        print('PART 1:', problem1(f'input/{DAY}.in'))
        print('PART 2:', problem2(f'input/{DAY}.in'))
