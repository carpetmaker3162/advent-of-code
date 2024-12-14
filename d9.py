DAY = 9

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
    s=lines[0]
    f=['.' for i in range(sum(map(int,list(s))))]
    curr=0
    ptr=0
    for i in range(len(s)):
        if i&1:
            ptr+=int(s[i])
        else:
            for _ in range(int(s[i])):
                f[ptr]=curr
                ptr+=1
            curr+=1
    left=0
    right=len(f)-1
    while left<=right:
        while left<len(f) and f[left]!='.': left+=1
        while right>0 and f[right]=='.': right-=1
        if left<=right:
            f[left],f[right]=f[right],f[left]
    for i in range(len(f)):
        if type(f[i])==int:
            ans+=i*f[i]
    return ans


def problem2(file):
    ans = 0
    lines = []

    with open(file) as f:
        for l in f.readlines():
            lines.append(l.strip())
    s=lines[0]
    f=['.' for i in range(sum(map(int,list(s))))]
    curr=0
    ptr=0
    files=[]
    spaces=[]
    for i in range(len(s)):
        if i&1:
            spaces.append((ptr,int(s[i])))
            ptr+=int(s[i])
        else:
            files.append((ptr,int(s[i])))
            for _ in range(int(s[i])):
                f[ptr]=curr
                ptr+=1
            curr+=1
    for loc,leng in files[::-1]:
        for i,ss in enumerate(spaces):
            dest,sp=ss
            if sp>=leng and dest<loc:
                f[dest:dest+leng]=f[loc:loc+leng]
                f[loc:loc+leng]=['.']*leng
                dest+=leng
                sp-=leng
                spaces[i]=(dest,sp)
                break
    for i in range(len(f)):
        if type(f[i])==int:
            ans+=i*f[i]
    return ans


if __name__ == '__main__':
    if 'debug' in sys.argv:
        print('PART 1:', problem1('input.txt'))
        print('PART 2:', problem2('input.txt'))
    else:
        print('PART 1:', problem1(f'input/{DAY}.in'))
        print('PART 2:', problem2(f'input/{DAY}.in'))
