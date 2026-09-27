import sys

def found_degree(s,step = 0):

    if (len(s) == 1):
        if s == '9':
            return max(1,step)
        else:
            return 0

    sum_digit = sum(map(int,s))

    return found_degree(str(sum_digit),step + 1)

def main():

    input_data = sys.stdin.read().split()

    for s in input_data:

        if s == '0':
            break

        step = found_degree(s)

        if step == 0:
            print(f'{s} is not a multiple of 9.')
        else:
            print(f"{s} is a multiple of 9 and has 9-degree {step}.")

if __name__ == '__main__':
    main()