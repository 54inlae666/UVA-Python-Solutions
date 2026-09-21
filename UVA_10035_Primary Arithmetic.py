import sys

def solve():

    lines = sys.stdin.read().splitlines()
    for line in lines:

        line = line.strip()
        if not line:
            continue

        a,b = map(int,line.split())

        if a == 0 and b == 0:
            break
        
        carry_times = 0
        carry = 0

        while a > 0 or b > 0:

            a,digit_a = divmod(a,10)
            b,digit_b = divmod(b,10)

            current_sum = digit_a + digit_b + carry
            carry = current_sum // 10
            carry_times += carry 

        if carry_times > 1:
            print(f"{carry_times} carry operations.")
        elif carry_times == 1:
            print("1 carry operation.")
        else:
            print("No carry operation.")

if __name__ == "__main__":
    solve()