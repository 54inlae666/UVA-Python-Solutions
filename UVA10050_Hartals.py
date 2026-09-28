import sys

def solve():

    input_data = iter(sys.stdin.read().split())

    T = int(next(input_data))

    current_case = 1
    while current_case <= T:

        N = int(next(input_data)) #total days
        days_list = [0] * N
        
        P = int(next(input_data)) #number of parties

        for _ in range(P):
            strikes_T = int(next(input_data))
            for idx in range(strikes_T - 1,N,strikes_T):
                if idx % 7 != 5 and idx % 7 != 6:
                    days_list[idx] = 1 

        print(days_list.count(1))
        current_case += 1

if __name__ == "__main__":
    solve()