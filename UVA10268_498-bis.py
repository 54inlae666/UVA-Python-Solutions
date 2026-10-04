import sys

def solve():
    lines = iter(sys.stdin.read().splitlines())
    for line in lines:
        x = int(line.strip())
        poly = list(map(int,next(lines).split()))
        hp = len(poly) - 1

        ans = 0
        for idx in range(hp):QC
            ans = (ans * x) + ((hp - idx) * poly[idx])
        print(ans)

if __name__ == "__main__":
    solve()