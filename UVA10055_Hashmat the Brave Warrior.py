import sys

def solve():
    # 利用 sys.stdin 讀取所有輸入，直到 EOF 為止
    for line in sys.stdin:
        # 若讀取到空行則跳過
        if not line.strip():
            continue

        # 解析兩個數字
        vassal, opponent = map(int, line.split())

        # 計算絕對差值並輸出
        print(abs(vassal - opponent))


if __name__ == "__main__":
    solve()