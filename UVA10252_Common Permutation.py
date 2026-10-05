import sys
from collections import Counter

if __name__ == "__main__":

    lines = sys.stdin.read().split("\n")

    for idx in range(0,len(lines),2):
        if (idx + 1) < len(lines):
            count_a = Counter(lines[idx].strip())
            count_b = Counter(lines[idx + 1].strip())

            common = count_a & count_b

            print("".join(sorted(common.elements())))
