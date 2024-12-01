DAY = 1

import sys
import math
import re

def pr(x, **kwargs):
    print(x, **kwargs)
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

    a=[]
    b=[]
    for l in lines:
        aa,bb=ints(l)
        a.append(aa)
        b.append(bb)
    a.sort()
    b.sort()
    for i in range(len(a)):
        ans+=abs(a[i]-b[i])

    return ans

def problem2(file):
    ans = 0
    lines = []

    with open(file) as f:
        for l in f.readlines():
            lines.append(l.strip())

    a=[]
    b=[]
    for l in lines:
        aa,bb=ints(l)
        a.append(aa), b.append(bb)
    f=[0 for i in range(max(b)+1)]
    for n in b:
        f[n]+=1
    for n in a:
        ans+=n*f[n]

    return ans

if __name__ == "__main__":
    if "debug" in sys.argv:
        print("PART 1:", problem1("input.txt"))
        print("PART 2:", problem2("input.txt"))
    else:
        print("PART 1:", problem1(f"input/{DAY}.in"))
        print("PART 2:", problem2(f"input/{DAY}.in"))
