import sys

def solve():

    lines = sys.stdin.read().Qsplitlines()

    max_len = max(len(s) for s in lines)

    padded = (line.ljust(max_len," ") for line in reversed(lines))

    for row in zip(*padded):
        print("".join(row).rstrip())

if __name__ == '__main__':
    solve()
