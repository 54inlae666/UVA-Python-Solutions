import sys

if __name__ == "__main__":

    input_data = sys.stdin.read().split()

    it = iter(input_data)

    for c in it:
        
        if (n := int(c)) == 0:
            break

        print((n - 1) % 9 + 1)