import sys

def solve():
    input_data = iter(sys.stdin.read().split())

    T = int(next(input_data))
    #case:n
    for current_case in range(1,T + 1):
        print(f"Case {current_case}:")
        #將輸入costs存進list
        VALUES = [int(next(input_data)) for _ in range(36)]
        n_of_Q = int(next(input_data))
        #將Q存入list
        Q_list = [int(next(input_data)) for _ in range(n_of_Q)]
        #將list中的Q取出
        for Q_org in Q_list:
            #窮舉計算costs
            costs_dict = {} #base:costs
            for current_base in range(2,37):
                #計算costs
                Q = Q_org
                costs = 0
                if Q_org != 0:
                    while(Q > 0):
                        costs += VALUES[Q % current_base]
                        Q //= current_base
                else:
                    costs = VALUES[0]
                #把costs放入dict
                costs_dict[current_base] = costs
                #計算最低costs與輸出次數
            min_cost = min(costs_dict.values())

            cheapest_bases = [str(base) for base,cost in costs_dict.items() if cost == min_cost]

            ans_str = '' '.join(cheapest_bases)
            print(f"Cheapest base(s) for number {Q_org}: {ans_str}")    
            
if __name__ == "__main__":
    solve()
