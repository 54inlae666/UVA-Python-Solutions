import sys


FACE_MAP={
    'N' : ( 0, 1),
    'E' : ( 1, 0),
    'S' : ( 0,-1),
    'W' : (-1, 0)
}
DIRECTIONS = ['N', 'E', 'S', 'W']
flag_point = set()

def solve():
    lines = iter(sys.stdin.read().splitlines())
    max_X,max_Y = map(int,next(lines).split())

    for line in lines:
        if not line:
            continue
        curr_x,curr_y,facing = line.split()
        curr_x = int(curr_x)
        curr_y = int(curr_y)
        instr_str = next(lines).strip()
        gg_flag = False

        for instr in instr_str:
            if instr == 'R':
                facing = DIRECTIONS[(DIRECTIONS.index(facing) + 1) % 4]
            elif instr == 'L':
                facing = DIRECTIONS[(DIRECTIONS.index(facing) - 1) % 4]
            else: #指令 = F
                move_x,move_y = FACE_MAP[facing]

                if 0 <= (curr_x + move_x) <= max_X and 0 <= (curr_y + move_y) <= max_Y:
                        curr_x += move_x
                        curr_y += move_y
                else:
                    if (curr_x, curr_y) in flag_point:
                        continue
                    else:
                        flag_point.add((curr_x, curr_y))
                        gg_flag = True
                        break

        if gg_flag:
            print(f"{curr_x} {curr_y} {facing} LOST")
        else:
            print(f"{curr_x} {curr_y} {facing}")

if __name__ == "__main__":
    solve()