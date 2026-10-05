import sys

def solve():
    lines = sys.stdin.read().splitlines()
    if not lines:
        return
    
    n = int(lines[0])
    country_counts = {}

    for i in range(1, n + 1):
        line = lines[i].strip()
        if not line:
            continue
        
        country = line.split(maxsplit=1)[0]
        
        if country in country_counts:
            country_counts[country] += 1
        else:
            country_counts[country] = 1

    for country in sorted(country_counts.keys()):
        print(f"{country} {country_counts[country]}")

if __name__ == "__main__":
    solve()