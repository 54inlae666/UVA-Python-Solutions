import sys
import math

if __name__ == "__main__":

    lines = sys.stdin.read().splitlines()

    for line in lines:

        a,b = map(int,line.split())
        if a == 0 and b == 0:
            break

        start = math.ceil(math.sqrt(a))
        end = math.floor(math.sqrt(b))

        ans = end - start + 1

        print(ans)