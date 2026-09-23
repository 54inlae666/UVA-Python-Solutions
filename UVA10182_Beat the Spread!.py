import sys

if __name__ == "__main__":

    lines = sys.stdin.read().splitlines()

    test_case = int(lines[0])

    for idx in range(1,test_case + 1):
        
        line = lines[idx].split()
        s = int(line[0])
        d = int(line[1])

        if d > s or (s + d) & 1:
            print("impossible")
        else:
            a = (s + d) // 2
            b = (s - d) // 2

            print(f"{a} {b}")