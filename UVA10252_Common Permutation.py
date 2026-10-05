import sys
from collections import Counter

if __name__ == "__main__":

    lines = sys.stdin.read().splitlines()

    for idx in range(0,len(lines),2):
        if (idx + 1) < len(lines):
            count_a = Counter(lines[idx])
            count_b = Counter(lines[idx + 1])

            common = count_a & count_b

            print("".join(sorted(common.elements())))
