import sys

def solve():

    input_data = iter(sys.stdin.read().split())
    n_of_case = int(next(input_data))

    for current_case in range(1,n_of_case + 1):
        next(input_data)
        next(input_data)
        N = int(next(input_data))

        metric = [int(next(input_data)) for _ in range(N*N)]
        is_symmetric = all(
            metric[k] >= 0 and metric[k] == metric[N*N - 1 - k]
            for k in range(N*N)
        )
        
        if is_symmetric:
            print(f"Test #{current_case}: Symmetric.")
        else:
            print(f"Test #{current_case}: Non-symmetric.")

if __name__ == "__main__":
    solve()