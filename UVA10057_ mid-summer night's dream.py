import sys

def solve():
    input_data = iter(sys.stdin.read().split())

    for fsin_str in input_data:
        n_of_case = int(fsin_str)

        a_list = []
        for _ in range(n_of_case):
            a_str = next(input_data)
            a_list.append(int(a_str))

        a_list.sort()
        a_list_len = len(a_list)

        low_fsin = a_list[(a_list_len - 1) // 2]
        hight_fsin = a_list[a_list_len // 2]

        ans1 = low_fsin

        if low_fsin == hight_fsin:
            ans2 = a_list.count(low_fsin)
        else:
            ans2 = a_list.count(low_fsin) + a_list.count(hight_fsin)

        ans3 = hight_fsin - low_fsin + 1

        print(f"{ans1} {ans2} {ans3}")

if __name__ == "__main__":
    solve()