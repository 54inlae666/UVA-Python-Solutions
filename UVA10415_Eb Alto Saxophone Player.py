import sys

note_map = {
    'c' : {2,3,4,7,8,9,10},
    'd' : {2,3,4,7,8,9},
    'e' : {2,3,4,7,8},
    'f' : {2,3,4,7},
    'g' : {2,3,4},
    'a' : {2,3},
    'b' : {2},
    'C' : {3},
    'D' : {1,2,3,4,7,8,9},
    'E' : {1,2,3,4,7,8},
    'F' : {1,2,3,4,7},
    'G' : {1,2,3,4},
    'A' : {1,2,3},
    'B' : {1,2}
}

def solve():

    input_data = sys.stdin.read().splitlines()

    for idx in range(1,int(input_data[0]) + 1):

        press_count = [0] * 11
        previous_press = set()

        for note in input_data[idx]:

            current_press = note_map[note]

            newly_press = current_press - previous_press

            for key in newly_press:
                
                press_count[key] += 1

            previous_press = current_press

        print(*press_count[1:])

if __name__ == '__main__':
    solve()
