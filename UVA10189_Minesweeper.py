import sys

MOVE_INDEX = [
    (-1, 1),( 0, 1),( 1, 1),
    (-1, 0),        ( 1, 0),
    (-1,-1),( 0,-1),( 1,-1)
]

def solve():
    
    lines = iter(sys.stdin.read().splitlines())

    current_case = 1
    for line in lines:
        m,n = map(int,line.split())
        if not m | n :
            break
            
        if current_case != 1:
            print()

        field = []
        for _ in range(m):
            row_str = next(lines)
            field.append(list(row_str))

        result = [[0] * n for _ in range(m)]
        for idx_y in range(m):
            for idx_x in range(n):
                if field[idx_y][idx_x] == '*':
                    result[idx_y][idx_x] = '*'
                    for move_x,move_y in MOVE_INDEX:
                        shift_x,shift_y = idx_x + move_x,idx_y + move_y
                        if 0 <= shift_x < n and 0 <= shift_y < m and result[shift_y][shift_x] != '*':
                            result[shift_y][shift_x] += 1
        
        print(f"Field #{current_case}:")
        print("\n".join("".join(map(str,row)) for row in result))
        current_case += 1

if __name__ == "__main__":
    solve()