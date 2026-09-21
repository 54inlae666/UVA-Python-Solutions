import sys

def solve():
    # 讀取所有輸入
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    num_test_cases = int(input_data[0])
    idx = 1

    for _ in range(num_test_cases):
        # 讀取親戚數量
        r = int(input_data[idx])
        # 提取該組的門牌號碼並排序
        streets = sorted([int(x) for x in input_data[idx + 1 : idx + 1 + r]])
        idx += 1 + r

        # 找出中位數作為 Vito 的家
        vito_house = streets[r // 2]

        # 計算所有親戚到 Vito 家的距離總和
        total_distance = sum(abs(s - vito_house) for s in streets)

        print(total_distance)


if __name__ == "__main__":
    solve()
