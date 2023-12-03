DAY = 1

import sys
import math

def problem1(file):
    result=0
    with open(file) as f:
        for l in f.readlines():
            val=0
            for c in l:
                if c.isnumeric():
                    val+=int(c)*10
                    break
            for c in l[::-1]:
                if c.isnumeric():
                    val+=int(c)
                    break
            result+=val
    return result

def problem2(file):
    d=["one","two","three","four","five","six","seven","eight","nine"]
    ds={k:v+1 for v,k in enumerate(d)}
    for i in range(1,10):
        ds[str(i)]=i
    def idx(s,c,reverse=False):
        if c in s:
            if not reverse:
                return s.index(c)
            else:
                return len(s)-s[::-1].index(c[::-1])-len(c)
        else:
            return -1
    result=0
    with open(file) as f:
        for l in f.readlines():
            ft=[*filter(lambda a: idx(l,a)!=-1,[*ds.keys()])]
            digit1=ds[min(ft,key=lambda a: idx(l,a))]
            digit2=ds[max(ft,key=lambda a: idx(l,a,reverse=True))]
            result+=digit1*10+digit2
    return result

if __name__ == "__main__":
    if "debug" in sys.argv:
        print("PART 1:", problem1("input.txt"))
        print("PART 2:", problem2("input.txt"))
    else:
        print("PART 1:", problem1(f"input/{DAY}.in"))
        print("PART 2:", problem2(f"input/{DAY}.in"))
