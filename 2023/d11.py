DAY = 11

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

def insert_row(i,lines):
    lines.insert(i,"."*len(lines[0]))

def insert_col(i,lines):
    for j in range(len(lines)):
        a=list(lines[j])
        a.insert(i,".")
        lines[j]="".join(a)

def problem1(file):
    ans = 0
    lines = []

    with open(file) as f:
        for l in f.readlines():
            lines.append(l.strip())
    r=0
    while r<len(lines):
        if all(x!="#" for x in lines[r]):
            insert_row(r,lines)
            r+=2
        else:
            r+=1
    
    c=0
    while c<len(lines[0]):
        if all(x!="#" for x in "".join(r[c] for r in lines)):
            insert_col(c,lines)
            c+=2
        else:
            c+=1
    for l in lines:
        print("".join(l))

    return ans

def problem2(file):
    ans = 0
    lines = []

    with open(file) as f:
        for l in f.readlines():
            lines.append(l.strip())

    return ans

if __name__ == "__main__":
    if "debug" in sys.argv:
        print("PART 1:", problem1("input.txt"))
        print("PART 2:", problem2("input.txt"))
    else:
        print("PART 1:", problem1(f"input/{DAY}.in"))
        print("PART 2:", problem2(f"input/{DAY}.in"))

