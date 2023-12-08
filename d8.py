DAY = 8

import sys
import math
import re
import functools

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
    adj = {} # i mean this is basically a graph

    with open(file) as f:
        ls = f.readlines()
        cmds = ls[0].strip()
        for l in ls[2:]:
            a,b,c=l[0:3],l[7:10],l[12:15]
            adj[a]=(b,c)
    i = 0
    curr="AAA"
    while True:
        cmd=cmds[i%len(cmds)]
        if cmd=="L":
            curr=adj[curr][0]
        else:
            curr=adj[curr][1]
        i+=1
        if curr=="ZZZ":
            break

    return i

def problem2(file):
    ans = 0
    adj = {} # i mean this is basically a graph

    with open(file) as f:
        ls = f.readlines()
        cmds = ls[0].strip()
        for l in ls[2:]:
            a,b,c=l[0:3],l[7:10],l[12:15]
            adj[a]=(b,c)
    currs=[x for x in adj.keys() if x.endswith("A")]
    def solve(curr):
        i=0
        while True:
            cmd=cmds[i%len(cmds)]
            if cmd=="L":
                curr=adj[curr][0]
            else:
                curr=adj[curr][1]
            i+=1
            if curr.endswith("Z"):
                break
        return i
    return functools.reduce(math.lcm, map(solve, currs))

if __name__ == "__main__":
    if "debug" in sys.argv:
        print("PART 1:", problem1("input.txt"))
        print("PART 2:", problem2("input.txt"))
    else:
        print("PART 1:", problem1(f"input/{DAY}.in"))
        print("PART 2:", problem2(f"input/{DAY}.in"))

