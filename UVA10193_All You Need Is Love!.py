import sys
import math

def solve():
    input_data = iter(sys.stdin.read().splitlines())

    N = int(next(input_data))

    current_case = 1
    while current_case <= N:
        S1 = int(next(input_data),2)
        S2 = int(next(input_data),2)

        Flag = True if math.gcd(S1,S2) > 1 else False

        if Flag:
            print(f"Pair #{current_case}: All you need is love!")
        else:
            print(f"Pair #{current_case}: Love is not all you need!")
        current_case += 1

if __name__ == "__main__":
    solve()