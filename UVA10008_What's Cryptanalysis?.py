import sys
from collections import Counter

if __name__ == "__main__":

    input_data = sys.stdin.read()

    upper_counter = Counter(c.upper() for c in input_data if c.isalpha())

    result = sorted(upper_counter.items(),key = lambda x : (-x[1],x[0]))

    for a,b in result:
        print(f"{a} {b}")