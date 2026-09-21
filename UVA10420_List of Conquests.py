import sys

def solve():
    # 一次讀取所有行
    lines = sys.stdin.read().splitlines()
    if not lines:
        return
    
    # 第一行通常是筆數 N，我們從第二行開始讀取
    n = int(lines[0])
    country_counts = {}

    for i in range(1, n + 1):
        line = lines[i].strip()
        if not line:
            continue
        
        # 只切出第一個單字作為國家名稱，後面的名字直接不管
        # line.split(maxsplit=1) 表示最多只切一刀
        country = line.split()[0]
        
        # 進行字典計數
        if country in country_counts:
            country_counts[country] += 1
        else:
            country_counts[country] = 1

    # 排序並輸出結果
    for country in sorted(country_counts.keys()):
        print(f"{country} {country_counts[country]}")

if __name__ == "__main__":
    solve()