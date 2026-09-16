import sys

# 使用全域字典作為記憶化快取 (Memoization Cache)
# 基礎條件：1 的鏈長為 1
memo = {1: 1}


def get_cycle_length(n):
    # 如果這個數字曾經計算過，直接回傳快取結果！(O(1) 時間)
    if n in memo:
        return memo[n]

    # 利用遞歸或迭代計算，並記錄結果
    # 奇數：3n + 1，偶數：n >> 1
    if n & 1:
        next_n = 3 * n + 1
    else:
        next_n = n >> 1

    # 當前數字的鏈長 = 1 + 下一個數字的鏈長
    length = 1 + get_cycle_length(next_n)

    # 寫入字典，備日後查詢
    memo[n] = length
    return length


def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    it = iter(input_data)
    for start_str in it:
        end_str = next(it)

        orig_start = int(start_str)
        orig_end = int(end_str)

        search_min = min(orig_start, orig_end)
        search_max = max(orig_start, orig_end)

        max_len = 0
        for n in range(search_min, search_max + 1):
            length = get_cycle_length(n)
            if length > max_len:
                max_len = length

        print(f"{orig_start} {orig_end} {max_len}")


if __name__ == "__main__":
    main()
