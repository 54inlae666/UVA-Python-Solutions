import sys
from collections import Counter

def solve():
    lines = sys.stdin.read().splitlines()

    print_space = False
    for line in lines:
        if not line:
            continue
        if print_space:
            print()
            
        a_counter = Counter(line)

        sorted_list = sorted(a_counter.items(),key=lambda x:(x[1],-ord(x[0])))

        for char,frequencies in sorted_list:
            print(f"{ord(char)} {frequencies}")
        print_space = True

if __name__ == "__main__":
    solve()
