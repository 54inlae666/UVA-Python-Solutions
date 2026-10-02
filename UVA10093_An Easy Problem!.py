import sys
import random

def solve():
        CHAR_MAP = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        VAL_DICT = {char_fsin:val_fsin for val_fsin,char_fsin in enumerate(CHAR_MAP)}

        input_data = sys.stdin.read().split()

        for line in input_data:
            R = 0
            R = sum(VAL_DICT.get(c, 0) for c in line)
            max_val = max((VAL_DICT.get(c, 0) for c in line), default=0)
            start = max(2, max_val + 1)
        
            for N in range(start,63):
                if R % (N - 1) == 0:
                    ans = N
                    print(ans)
                    break
            else:
                print("such number is impossible!")
   
if __name__ == "__main__":
    solve()