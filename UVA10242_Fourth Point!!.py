import sys



def solve():

    input_data = sys.stdin.read().splitlines()

    for line in input_data:
        data = iter(line.split())
        position_list = []
        for _ in range(4):
            x_str = next(data)
            y_str = next(data)
            x,y=float(x_str),float(y_str)
            p = (x,y)

            position_list.append(p)

        p1, p2, p3, p4 = position_list

        if p1 == p3:
            A, B, C = p2, p1, p4
        elif p1 == p4:
            A, B, C = p2, p1, p3
        elif p2 == p3:
            A, B, C = p1, p2, p4
        else:
            A, B, C = p1, p2, p3
        
        ax, ay = A
        bx, by = B
        cx, cy = C

        ans_x = ax + cx - bx
        ans_y = ay + cy - by

        print(f"{ans_x:.3f} {ans_y:.3f}")    

if __name__ == "__main__":
    solve()