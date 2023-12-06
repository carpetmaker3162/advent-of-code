DAY = 6

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
    lines=[]

    with open(file) as f:
        for l in f.readlines():
            lines.append(l)
    times=ints(lines[0])
    dists=ints(lines[1])
    for i in range(len(times)):
        t, d = times[i], dists[i]
        r1 = ((-t - math.sqrt(t**2 - 4*d)) / -2)
        r2 = ((-t + math.sqrt(t**2 - 4*d)) / -2)
        r1,r2=math.floor(min(r1,r2)),math.ceil(max(r1,r2))
        w=r2-r1-1
        if ans==0:
            ans=w
        else:
            ans*=w

    return ans

def problem2(file):
    ans = 0
    lines=[]

    with open(file) as f:
        for l in f.readlines():
            lines.append("".join(x for x in l if x != " "))
    times=ints(lines[0])
    dists=ints(lines[1])
    for i in range(len(times)):
        t, d = times[i], dists[i]
        r1 = ((-t - math.sqrt(t**2 - 4*d)) / -2)
        r2 = ((-t + math.sqrt(t**2 - 4*d)) / -2)
        r1,r2=math.floor(min(r1,r2)),math.ceil(max(r1,r2))
        w=r2-r1-1
        if ans==0:
            ans=w
        else:
            ans*=w

    return ans

if __name__ == "__main__":
    if "debug" in sys.argv:
        print("PART 1:", problem1("input.txt"))
        print("PART 2:", problem2("input.txt"))
    else:
        print("PART 1:", problem1(f"input/{DAY}.in"))
        print("PART 2:", problem2(f"input/{DAY}.in"))

