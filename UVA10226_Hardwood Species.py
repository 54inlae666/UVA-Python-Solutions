import sys
from collections import Counter

def solve():

    input_data = iter(sys.stdin.read().splitlines())

    T = int(next(input_data))
    next(input_data)

    current_case = 1
    while current_case <= T:
        species_counter = Counter()
        total_count = 0

        while True:
            line = next(input_data,None)
            if line is None or line.strip() == "":
                break
            line = line.strip()
            total_count += 1
            species_counter[line] += 1

        for tree in sorted(species_counter.keys()):
            percent = species_counter[tree] / total_count * 100
            print(f"{tree} {percent:.4f}")

        if current_case < T:
            print()

        current_case += 1

if __name__ == "__main__":
    solve()