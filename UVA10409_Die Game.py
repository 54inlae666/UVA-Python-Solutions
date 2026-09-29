import sys



def solve():
    lines = iter(sys.stdin.read().split())
    for line in lines:
        case_count = int(line.strip())
        if case_count == 0:
            break

        t = 1
        n = 2
        w = 3

        for _ in range(case_count):
            command = next(lines)
            if command == "north":
                t,n,w = 7 - n,t,w
            elif command == "south":
                t,n,w = n,7 - t,w
            elif command == "east":
                t,n,w = w,n,7 - t
            else:
                t,n,w = 7 - w,n,t

        print(t)
if __name__ == "__main__":
    solve()
