import sys


def solve():
    # 讀取標準輸入的所有內容（包含換行符號）
    input_data = sys.stdin.read()

    # 狀態旗標：True 表示下一個遇到的 '"' 是開引號
    first_quote = True
    output = []

    for char in input_data:
        if char == '"':
            if first_quote:
                output.append("``")
            else:
                output.append("''")
            # 切換狀態
            first_quote = not first_quote
        else:
            # 不是雙引號，原樣保留
            output.append(char)

    # 將字元陣列組合回字串並印出
    print("".join(output), end="")


if __name__ == "__main__":
    solve()