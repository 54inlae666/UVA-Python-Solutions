import sys

def c_mod(n,M):

    return n % M if n >= 0 else -(-n % M)

def get_sort_key(n,M):

    n_mod = c_mod(n,M)
    is_odd = (n & 1)

    if is_odd == 1:
        return(n_mod,0,-n)
    else:
        return(n_mod,1,n)

def solve():

    input_data = sys.stdin.read().split()

    ptr = 0
    total_len = len(input_data)

    while ptr < total_len - 2:

        case_number = int(input_data[ptr])
        M = int(input_data[ptr + 1])
        ptr += 2

        print(f"{case_number} {M}")

        n_list = list(map(int,input_data[ptr:ptr + case_number]))

        ptr += case_number

        n_list.sort(key = lambda n : get_sort_key(n,M))

        if n_list:
            print('\n'.join(map(str,n_list)))
    
    print("0 0")
    
if __name__ == '__main__':
    solve()
