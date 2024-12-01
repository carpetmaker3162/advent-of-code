DAY = 7

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

ordering = "23456789TJQKA"
ordering2 = "J23456789TQKA" # bruh...

def freqs(s):
    vis = []
    res = []
    for c in s:
        if c in vis:
            continue
        res.append(s.count(c))
        vis.append(c)
    res.sort(reverse=True)
    return res

def maxfreql(s):
    l=list(s)
    l.sort(key=lambda a: s.count(a),reverse=True)
    for c in l:
        if c!="J":
            return c
    return "J"

# higher if stronger
def find_type(c):
    f = freqs(c)
    assert sum(f) == 5
    if len(f) > 0 and f[0] == 5:
        return 7
    elif len(f) > 1 and f[0] == 4 and f[1] == 1:
        return 6
    elif len(f) > 1 and f[0] == 3 and f[1] == 2:
        return 5
    elif len(f) > 2 and f[0] == 3 and f[1] == 1 and f[2] == 1:
        return 4
    elif len(f) > 2 and f[0] == 2 and f[1] == 2 and f[2] == 1:
        return 3
    elif len(f) > 3 and f[0] == 2 and f[1] == 1 and f[2] == 1 and f[3] == 1:
        return 2
    else:
        return 1

assert find_type("AAAAA") == 7
assert find_type("AA8AA") == 6
assert find_type("23332") == 5
assert find_type("TTT98") == 4
assert find_type("23432") == 3
assert find_type("A23A4") == 2
assert find_type("23456") == 1

def problem1(file):
    ans = 0
    plays=[]

    with open(file) as f:
        for l in f.readlines():
            card,bid=l.split()
            bid=int(bid)
            plays.append((card,bid))
    plays.sort(key=lambda a: (find_type(a[0]), tuple(ordering.index(c) for c in a[0])))
    for i,play in enumerate(plays):
        card,bid=play
        ans+=(i+1)*bid

    return ans

def problem2(file):
    ans = 0
    plays=[]

    with open(file) as f:
        for l in f.readlines():
            card,bid=l.split()
            bid=int(bid)
            plays.append((card,bid))
    plays.sort(key=lambda a: (find_type(a[0].replace("J",maxfreql(a[0]))), tuple(ordering2.index(c) for c in a[0])))
    for i,play in enumerate(plays):
        card,bid=play
        ans+=(i+1)*bid

    return ans

if __name__ == "__main__":
    if "debug" in sys.argv:
        print("PART 1:", problem1("input.txt"))
        print("PART 2:", problem2("input.txt"))
    else:
        print("PART 1:", problem1(f"input/{DAY}.in"))
        print("PART 2:", problem2(f"input/{DAY}.in"))

