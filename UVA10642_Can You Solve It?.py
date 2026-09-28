import sys

def solve():

    input_data = iter(sys.stdin.read().splitlines())
    N = int(next(input_data))

    for current_case in range(1,N + 1):
        point_data = next(input_data).split()
        x1,y1,x2,y2 = map(int,point_data)
        p1 = (x1 + y1) * (x1 + y1 + 1) // 2 + x1
        p2 = (x2 + y2) * (x2 + y2 + 1) // 2 + x2
        print(f"Case {current_case}: {abs(p2-p1)}")

if __name__ == "__main__":
    solve()