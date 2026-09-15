import sys

def solve():

    input_data = sys.stdin.read().split()

    it = iter(input_data)
    for v_str in it:
        t_str = next(it)
        v = int(v_str)
        t = int(t_str)
        print(2 * v * t)

if __name__ == "__main__":
    solve()