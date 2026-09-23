import sys

if __name__ == "__main__":

    input_data = sys.stdin.read().split()

    for c in input_data:

        n = int(c)
        
        print(n + n // 2)