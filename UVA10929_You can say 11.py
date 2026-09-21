import sys

def solve():

    input_data = sys.stdin.read().split()
    it = iter(input_data)
    for n_str in it:

        if n_str == '0':
            break
                    
        odd_sum = sum(int(ch) for ch in n_str[0::2])
        even_sum = sum(int(ch) for ch in n_str[1::2])
        
        if abs(odd_sum - even_sum) % 11 == 0:
            print(f"{n_str} is a multiple of 11.")
        else:
            print(f"{n_str} is not a multiple of 11.")

if __name__ == "__main__":
    solve()
