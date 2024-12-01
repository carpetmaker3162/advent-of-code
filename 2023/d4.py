DAY = 4

import sys
import math
import re

def pr(x, **kwargs):
    print(x, **kwargs)
    return x

def uints(string):
    nums = re.finditer(r'\d+', string)
    return [(x.start(), int(string[x.start():x.end()])) for x in nums]

def ints(string):
    nums = re.finditer(r'-?\d+', string)
    return [(x.start(), int(string[x.start():x.end()])) for x in nums]

def problem1(file):
    ans = 0

    with open(file) as f:
        for l in f.readlines():
            colon=l.index(":")
            l=l[colon+1:].strip(" :")
            w,y=l.split("|")
            *w,=map(int,w.split())
            *y,=map(int,y.split())
            value=0
            for n in y:
                if n in w:
                    if value == 0:
                        value = 1
                    else:
                        value *= 2
            ans += value

    return ans

def problem2(file):
    ans = 0

    with open(file) as f:
        cards=[]
        maxcard=0
        for l in f.readlines():
            colon=l.index(":")
            idx=ints(l)[0][1]-1
            l=l[colon+1:].strip(" :")
            w,y=l.split("|")
            *w,=map(int,w.split())
            *y,=map(int,y.split())
            cards.append((idx,w,y))
            maxcard=max(maxcard,idx)+1
        counts=[1 for i in range(maxcard)]
        for idx,w,y in cards:
            count=0
            for n in y:
                if n in w:
                    count+=1
            for i in range(idx+1,idx+1+count):
                if i < len(counts):
                    counts[i] += counts[idx]
    return sum(counts)

if __name__ == "__main__":
    if "debug" in sys.argv:
        print("PART 1:", problem1(f"input.txt"))
        print("PART 2:", problem2(f"input.txt"))
    else:
        print("PART 1:", problem1(f"input/{DAY}.in"))
        print("PART 2:", problem2(f"input/{DAY}.in"))
