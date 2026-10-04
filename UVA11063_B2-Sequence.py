import sys

def solve():
    input_data = iter(sys.stdin.read().split())

    current_case = 1
    for n_str in input_data:
        n = int(n_str)
        b2_list = [int(next(input_data)) for _ in range(n)]

        is_b2_sequence = b2_list[0] > 0 and all(
            b2_list[idx] > b2_list[idx - 1]
            for idx in range(1,n)
        )
        if is_b2_sequence:
            add_set = set()
            for i in range(n):
                for j in range(i,n):
                    b2_add = b2_list[i] + b2_list[j]
                    if b2_add in add_set:
                        is_b2_sequence = False
                        break
                    add_set.add(b2_add)
                if not is_b2_sequence: break
        
        if is_b2_sequence:
            print(f"Case #{current_case}: It is a B2-Sequence.")
        else:
            print(f"Case #{current_case}: It is not a B2-Sequence.")
        print()
        current_case += 1

if __name__ == "__main__":
    solve()