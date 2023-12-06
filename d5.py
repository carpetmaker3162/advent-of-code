# advent of code is rapidly becoming reading comprehension
DAY = 5

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
    lines=[]
    
    def collect(idx):
        idx+=1
        res=[]
        while idx<len(lines) and lines[idx]:
            res.append(uints(lines[idx]))
            idx+=1
        return res

    def _map(num,dest,start,length):
        # 99 50 98 2
        # 98 99 100
        # 99-98+50=51
        if start<=num<start+length:
            return num-start+dest
        else:
            return None

    with open(file) as f:
        for l in f.readlines():
            lines.append(l.strip())
    seeds=uints(lines[0])
    rs1=collect(lines.index("seed-to-soil map:"))
    rs2=collect(lines.index("soil-to-fertilizer map:"))
    rs3=collect(lines.index("fertilizer-to-water map:"))
    rs4=collect(lines.index("water-to-light map:"))
    rs5=collect(lines.index("light-to-temperature map:"))
    rs6=collect(lines.index("temperature-to-humidity map:"))
    rs7=collect(lines.index("humidity-to-location map:"))

    def apply(num,rs):
        for dest,start,length in rs:
            mapped = _map(num,dest,start,length)
            if mapped is not None:
                num = mapped
                break
        return num

    def applyall(num):
        num=apply(num,rs1)
        num=apply(num,rs2)
        num=apply(num,rs3)
        num=apply(num,rs4)
        num=apply(num,rs5)
        num=apply(num,rs6)
        num=apply(num,rs7)
        return num
    
    return applyall(min(seeds,key=applyall))

def problem2(file):
    # map ranges??
    ans = 0
    lines=[]

    def collect(idx):
        idx+=1
        res=[]
        while idx<len(lines) and lines[idx]:
            res.append(uints(lines[idx]))
            idx+=1
        return res

    def fmt_range(range_beginning, range_end):
        return (range_beginning, range_end - range_beginning)

    with open(file) as f:
        for l in f.readlines():
            lines.append(l.strip())
    
    seeds=uints(lines[0])
    seedranges=[(seeds[2*i], seeds[2*i+1]) for i in range(len(seeds)//2)]
    filtergroups = []
    filtergroups.append(collect(lines.index("seed-to-soil map:")))
    filtergroups.append(collect(lines.index("soil-to-fertilizer map:")))
    filtergroups.append(collect(lines.index("fertilizer-to-water map:")))
    filtergroups.append(collect(lines.index("water-to-light map:")))
    filtergroups.append(collect(lines.index("light-to-temperature map:")))
    filtergroups.append(collect(lines.index("temperature-to-humidity map:")))
    filtergroups.append(collect(lines.index("humidity-to-location map:")))

    for filters in filtergroups:
        split_ranges = []
        for filter_dest, filter_start, filter_length in filters:
            unfiltered = []
            for seedrange in seedranges:
                range_start, range_length = seedrange
                range_end = range_start + range_length
                filter_end = filter_start + filter_length
                
                apply_start = max(range_start,filter_start)
                apply_end = min(range_end,filter_end)

                if apply_end - apply_start > 0:
                    split_ranges.append((apply_start-filter_start+filter_dest, apply_end-apply_start))
                    if range_start < filter_start:
                        unfiltered.append((range_start, filter_start - range_start))
                    if range_end > filter_end:
                        unfiltered.append((filter_end, range_end - filter_end))
                else:
                    unfiltered.append(seedrange)
            seedranges = unfiltered[:]
        seedranges.extend(split_ranges)
    
    return min(seedranges,key=lambda a: a[0])[0]

if __name__ == "__main__":
    if "debug" in sys.argv:
        print("PART 1:", problem1("input.txt"))
        print("PART 2:", problem2("input.txt"))
    else:
        print("PART 1:", problem1(f"input/{DAY}.in"))
        print("PART 2:", problem2(f"input/{DAY}.in"))

