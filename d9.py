DAY = 9

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

    with open(file) as f:
        for l in f.readlines():
            history=ints(l)
            h=[]
            h.append(history)
            while not all(x==0 for x in history):
                newhistory=[]
                for i in range(len(history)-1):
                    newhistory.append(history[i+1]-history[i])
                h.append(newhistory)
                history=newhistory[:]
            h=list(reversed(h))
            h[0].append(0)
            for i, hist in enumerate(h[1:]):
                h[i+1].append(hist[-1]+h[i][-1])
            ans+=h[-1][-1]

    return ans

def problem2(file):
    ans = 0

    with open(file) as f:
        for l in f.readlines():
            history=ints(l)
            h=[]
            h.append(history)
            while not all(x==0 for x in history):
                newhistory=[]
                for i in range(len(history)-1):
                    newhistory.append(history[i+1]-history[i])
                h.append(newhistory)
                history=newhistory[:]
            h=list(reversed(h))
            h[0].append(0)
            for i, hist in enumerate(h[1:]):
                h[i+1].insert(0,hist[0]-h[i][0])
            ans+=h[-1][0]

    return ans

if __name__ == "__main__":
    if "debug" in sys.argv:
        print("PART 1:", problem1("input.txt"))
        print("PART 2:", problem2("input.txt"))
    else:
        print("PART 1:", problem1(f"input/{DAY}.in"))
        print("PART 2:", problem2(f"input/{DAY}.in"))

