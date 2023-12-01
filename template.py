import sys
import math
import re

def pr(x, **kwargs):
    print(x, **kwargs)
    return x

def ints(string):
    nums = re.findall(r'\d+', string)
    return [*map(int, nums)]

def problem1(file):
    ans = 0

    with open(file) as f:
        for l in f.readlines():
            pass

    return ans

def problem2(file):
    ans = 0

    with open(file) as f:
        for l in f.readlines():
            pass

    return ans

if __name__ == "__main__":
    print("PART 1:", problem1(f"input/{DAY}.in"))
    print("PART 2:", problem2(f"input/{DAY}.in"))
