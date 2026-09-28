import sys
import math

def solve():

    MAX_N = 1000000

    is_prime_table = [True] * MAX_N
    is_prime_table[0] = False
    is_prime_table[1] = False

    for i in range(2,int(1000000 ** 0.5) + 1):
        if is_prime_table[i]:
            for j in range(i * i,1000000,i):
                is_prime_table[j] = False 

    input_data = sys.stdin.read().split()

    for str_n in input_data:
        n = int(str_n)
        reversed_n = int(str_n[::-1])
        if not is_prime_table[n]:
            print(f"{n} is not prime.")
        elif n != reversed_n and is_prime_table[reversed_n]:
            print(f"{n} is emirp.")
        else:
            print(f"{n} is prime.")


if __name__ == "__main__":
    solve()