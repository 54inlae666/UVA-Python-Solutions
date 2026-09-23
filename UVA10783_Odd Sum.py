import sys

if __name__ == "__main__":

    input_data = sys.stdin.read().split()

    case_number = int(input_data[0])
    idx = 1

    for case_n in range(1,case_number + 1):

        a = int(input_data[idx])
        b = int(input_data[idx + 1])
        idx += 2

        start = a + 1 if a & 1 == 0 else a
        end = b - 1 if b & 1 == 0 else b

        count = (end - start) // 2 + 1
        total = (start + end) * count // 2

        print(f"Case {case_n}: {total}")

