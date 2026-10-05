import sys

def solve():
    for line in sys.stdin:
        if not line.strip():
            continue

        vassal, opponent = map(int, line.split())
        
        print(abs(vassal - opponent))


if __name__ == "__main__":
    solve()