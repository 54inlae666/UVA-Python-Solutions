import sys
import math

def solve():
    lines = sys.stdin.read().splitlines()
    for line in lines:
        if not line:
            continue
        data = line.split()
        s = float(data[0])
        a = float(data[1])
        if data[2] == "min": a /= 60 
        if a > 360: a %= 360
        if a > 180: a = 360 - a
        r = 6440 + s
        hc = math.radians(a)
        print(f"{r * hc:.6f} {2 * r * math.sin(hc / 2):.6f}")

if __name__ == "__main__":
    solve()
