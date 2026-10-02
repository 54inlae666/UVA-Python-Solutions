import sys

def solve():
    input_data = iter(sys.stdin.read().split())

    T = int(next(input_data))

    for _ in range(T):
        M = int(next(input_data))
        N = int(next(input_data))
        Q = int(next(input_data))
        print(f"{M} {N} {Q}")
        grid = [next(input_data) for _ in range(M)]

        Q_list = []
        for _ in range(Q):
            r = int(next(input_data))
            c = int(next(input_data))

            center_char = grid[r][c]

            k = 1
            while r - k >=0 and r + k <M and c - k >= 0 and c + k < N:
                if all(
                    grid[i][j] == center_char
                    for i in range(r - k,r + k + 1)
                    for j in range(c - k,c + k + 1)
                ):
                    k += 1
                else:
                    break
            Q_list.append(str(2 * (k-1) + 1))

        print("\n".join(Q_list))


if __name__ == "__main__":
    solve()