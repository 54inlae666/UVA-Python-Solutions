import sys

memo = {1: 1}


def get_cycle_length(n):
 
    if n in memo:
        return memo[n]

    if n & 1:
        next_n = 3 * n + 1
    else:
        next_n = n >> 1

    length = 1 + get_cycle_length(next_n)

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
