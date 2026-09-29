import sys


def solve():
    input_data = sys.stdin.read()

    first_quote = True
    output = []

    for char in input_data:
        if char == '"':
            if first_quote:
                output.append("``")
            else:
                output.append("''")

            first_quote = not first_quote
        else:

            output.append(char)

    print("".join(output), end="")


if __name__ == "__main__":
    solve()