import sys

def solve():

    input_data = sys.stdin.read().split()

    case_number = int(input_data[0])

    for idx in range(1,case_number + 1):

        b1 = bin(int(input_data[idx])).count('1')

        b2 = bin(int(input_data[idx],16)).count('1')

        print(f"{b1} {b2}")

if __name__ == '__main__':
    solve()
