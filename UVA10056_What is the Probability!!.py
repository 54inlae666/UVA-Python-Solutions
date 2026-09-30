import sys

def solve():

    input_data = iter(sys.stdin.read().split())

    S = int(next(input_data))
    for _ in range(S):
        N = int(next(input_data))
        p = float(next(input_data))
        I = int(next(input_data))

        if p == 0:
            print("0.0000")
            continue

        a = ((1-p)**(I-1))*p
        r = (1-p)**N
        ans = a / (1 - r)

        print(f"{ans:.4f}")

if __name__ == "__main__":
    solve()