import sys
import math

if __name__ == "__main__":

    input_data = sys.stdin.read().split()

    it = iter(input_data)

    for c in it:

        if (n := int(c)) == 0:
            break
        
        ans = 0

        for j in range(2,n + 1):
            for i in range(1,j):
                ans += math.gcd(i,j)

        print(ans)