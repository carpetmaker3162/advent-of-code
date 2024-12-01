DAY = 10

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
    R = len(lines)
    C = len(lines[0])

    start = None
    for r, row in enumerate(lines):
        for c, cell in enumerate(row):
            if cell == "S":
                start = (r,c)
                break
    curr = start
    prev = start
    valid_to = {(0,1):"-J7",(0,-1):"-FL",(1,0):"|LJ",(-1,0):"|7F"}
    valid_from = {"L":[(0,1),(-1,0)],"J":[(0,-1),(-1,0)],"7":[(1,0),(0,-1)],"F":[(1,0),(0,1)],"-":[(0,-1),(0,1)],"|":[(-1,0),(1,0)]}
    while True:
        stop=False
        for d, vsqs in valid_to.items():
            r,c = curr
            dr,dc = d
            nr,nc = r+dr,c+dc
            if (nr,nc) == prev or not (0<=nr<R and 0<=nc<C):
                continue
            if lines[r][c] in "LJ7F|-" and (dr,dc) not in valid_from[lines[r][c]]:
                continue
            if lines[nr][nc] == "S":
                stop=True
                break
            if lines[nr][nc] in vsqs:
                prev = curr
                curr = (nr,nc)
                ans+=1
                break
        if stop:
            break
    
    return math.ceil(ans//2+1)

def problem2(file):
    ans = 0
    lines = []

    with open(file) as f:
        for l in f.readlines():
            lines.append(l.strip())
    R = len(lines)
    C = len(lines[0])
    path = [["." for i in row] for row in lines]

    start = None
    for r, row in enumerate(lines):
        for c, cell in enumerate(row):
            if cell == "S":
                start = (r,c)
                path[r][c] = "S"
                break
    curr = start
    prev = start
    valid_to = {(0,1):"-J7",(0,-1):"-FL",(1,0):"|LJ",(-1,0):"|7F"}
    valid_from = {"L":[(0,1),(-1,0)],"J":[(0,-1),(-1,0)],"7":[(1,0),(0,-1)],"F":[(1,0),(0,1)],"-":[(0,-1),(0,1)],"|":[(-1,0),(1,0)]}
    while True:
        stop=False
        for d, vsqs in valid_to.items():
            r,c = curr
            dr,dc = d
            nr,nc = r+dr,c+dc
            if (nr,nc) == prev or not (0<=nr<R and 0<=nc<C):
                continue
            if lines[r][c] in "LJ7F|-" and (dr,dc) not in valid_from[lines[r][c]]:
                continue
            if lines[nr][nc] == "S":
                stop=True
                break
            if lines[nr][nc] in vsqs:
                prev = curr
                curr = (nr,nc)
                path[nr][nc] = lines[nr][nc]
                break
        if stop:
            break

    sr,sc = start
    directions=set()
    for k, v in valid_to.items():
        r,c=k
        if path[sr+r][sc+c] in v:
            directions.add((r,c))
    valid_from["|"]=[(1,0),(-1,0)]
    valid_from["-"]=[(0,-1),(0,1)]
    for k, v in valid_from.items():
        if set(v)==directions:
            path[sr][sc]=k

    inside = False
    s=[]
    same={"J":"L","7":"F"}
    for r in range(R):
        row = path[r]
        for cell in row:
            if cell == "|":
                inside = not inside
            elif cell == ".":
                if inside:
                    ans+=1
            elif cell in "LF":
                s.append(cell)
            elif cell in "7J":
                pair=s.pop()
                if same[cell]==pair:
                    pass # ?
                else:
                    inside = not inside

    return ans

if __name__ == "__main__":
    if "debug" in sys.argv:
        print("PART 1:", problem1("input.txt"))
        print("PART 2:", problem2("input.txt"))
    else:
        print("PART 1:", problem1(f"input/{DAY}.in"))
        print("PART 2:", problem2(f"input/{DAY}.in"))

