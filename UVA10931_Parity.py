import sys

def solve():
    input_data = sys.stdin.read().split()

    for I_str in input_data:
        if I_str == '0':
            break
        I_org = int(I_str)
        I = f"{I_org:b}" #str
        count = I.count('1')
        print(f"The parity of {I} is {count} (mod 2).")

if __name__ == "__main__":
    solve()