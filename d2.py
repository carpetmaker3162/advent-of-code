DAY = 2

import sys
import math
import re

def pr(x, **kwargs):
    print(x, **kwargs)
    return x

def ints(string):
    nums = re.findall(r'\d+', string)
    return [*map(int, nums)]

# 07:24 (get better at reading bozo)
def problem1(file):
    ans = 0
    R=12
    G=13
    B=14

    with open(file) as f:
        for l in f.readlines():
            id=ints(l)[0]
            l=l[8:]
            r=0
            g=0
            b=0
            possible=True
            for group in l.split(";"):
                for cubes in group.split(","):
                    n,c=cubes.strip(" :").split()
                    n=int(n)
                    if c=="red":
                        if n>R: possible=False
                    elif c=="green":
                        if n>G: possible=False
                    elif c=="blue":
                        if n>B: possible=False
            if possible:
                ans+=id
    return ans

# 09:14
def problem2(file):
    ans = 0

    with open(file) as f:
        for l in f.readlines():
            id=ints(l)[0]
            l=l[8:]
            r=0
            g=0
            b=0
            possible=True
            for group in l.split(";"):
                for cubes in group.split(","):
                    n,c=cubes.strip(" :").split()
                    n=int(n)
                    if c=="red":
                        r=max(r,n)
                    elif c=="green":
                        g=max(g,n)
                    elif c=="blue":
                        b=max(b,n)
            if possible:
                ans+=r*g*b
    return ans

if __name__ == "__main__":
    if "debug" in sys.argv:
        print("PART 1:", problem1("input.txt"))
        print("PART 2:", problem2("input.txt"))
    else:
        print("PART 1:", problem1(f"input/{DAY}.in"))
        print("PART 2:", problem2(f"input/{DAY}.in"))
