import sys
import bisect

def solve():

    input_data = iter(sys.stdin.read().split())
    T = int(next(input_data))

    fib_list = [1,2]
    for _ in range(T):
        N_org = int(next(input_data))
        

        while fib_list[-1] < N_org:
            fib_list.append(fib_list[-1] + fib_list[-2])

        N = N_org
        start_idx = bisect.bisect_right(fib_list,N_org) - 1
        ans = []
        for idx in range(start_idx,-1,-1):
            if N >= fib_list[idx]:
                N -= fib_list[idx]
                ans.append('1')
            else:
                ans.append('0')
        
        ans = "".join(ans)
        print(f"{ans} (fib)")
        
if __name__ == "__main__":
    solve()
