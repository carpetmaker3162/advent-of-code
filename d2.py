DAY = 2

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

    for l in lines:
        l=ints(l)
        d=[]
        for i in range(len(l)-1):
            d.append(l[i+1]-l[i])
        if any(x==0 for x in d):
            continue  # unsafe
        if all(x>0 for x in d) or all(x<0 for x in d):
            if all(1<=abs(x)<=3 for x in d):
                ans+=1

    return ans

def problem2(file):
    ans = 0
    lines = []

    with open(file) as f:
        for l in f.readlines():
            lines.append(l.strip())

    for l in lines:
        ll=ints(l)
        for j in range(len(ll)):
            l=ll[:]
            l.pop(j)
            d=[]
            for i in range(len(l)-1):
                d.append(l[i+1]-l[i])
            if any(x==0 for x in d):
                continue
            if all(x>0 for x in d) or all(x<0 for x in d):
                if all(1<=abs(x)<=3 for x in d):
                    ans+=1
                    break

    return ans

if __name__ == "__main__":
    if "debug" in sys.argv:
        print("PART 1:", problem1("input.txt"))
        print("PART 2:", problem2("input.txt"))
    else:
        print("PART 1:", problem1(f"input/{DAY}.in"))
        print("PART 2:", problem2(f"input/{DAY}.in"))
