DAY = 3

import sys
import math
import re

def pr(x, **kwargs):
    print(x, **kwargs)
    return x

def ints(string):
    nums = re.finditer(r'\d+', string)
    return [(x.start(), string[x.start():x.end()]) for x in nums]

def find_adjs(numsline, symidx):
    nums = ints(numsline)
    res = []
    for start, num in nums:
        if start-1<=symidx<=start+len(str(num)):
            res.append((start, int(num)))
    return res

symbols = {'*', '=', '/', '#', '@', '$', '+', '&', '-', '%'}

# ??:?? (restarted)
def problem1(file):
    ans = 0
    grid=[]
    vis=[]

    with open(file) as f:
        for l in f.readlines():
            grid.append(l)
    for r, row in enumerate(grid):
        sym=[i for i, x in enumerate(row) if x in symbols]
        for s in sym:
            if r>0: # not first
                adjs = find_adjs(grid[r-1], s)
                for a in adjs:
                    if (r, *a) not in vis:
                        vis.append((r, *a))
                        ans += a[1]
            if r<len(grid)-1:
                adjs = find_adjs(grid[r+1], s)
                for a in adjs:
                    if (r, *a) not in vis:
                        vis.append((r, *a))
                        ans += a[1]
            adjs = find_adjs(grid[r], s)
            for a in adjs:
                if (r, *a) not in vis:
                    vis.append((r, *a))
                    ans += a[1]

    return ans

# ??:?? (restarted)
def problem2(file):
    ans = 0
    grid=[]

    with open(file) as f:
        for l in f.readlines():
            grid.append(l)
    for r, row in enumerate(grid):
        sym=[i for i, x in enumerate(row) if x in symbols]
        for s in sym:
            if row[s] != "*":
                continue
            temp=[]
            if r>0: # not first
                adjs = find_adjs(grid[r-1], s)
                for a in adjs:
                    temp.append((r, *a))
            if r<len(grid)-1:
                adjs = find_adjs(grid[r+1], s)
                for a in adjs:
                    temp.append((r, *a))
            adjs = find_adjs(grid[r], s)
            for a in adjs:
                temp.append((r, *a))
            this=1
            if len(temp) == 2:
                for _, _, num in temp:
                    this*=num
                ans += this

    return ans

if __name__ == "__main__":
    if "debug" in sys.argv:
        print("PART 1:", problem1(f"input.txt"))
        print("PART 2:", problem2(f"input.txt"))
    else:
        print("PART 1:", problem1(f"input/{DAY}.in"))
        print("PART 2:", problem2(f"input/{DAY}.in"))
