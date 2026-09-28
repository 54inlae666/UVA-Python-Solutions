import sys

def solve():
    lines = sys.stdin.read().splitlines()

    for line in lines:

        data = line.split()
        n_org = int(data[0])
        m_org = int(data[1])
        n = n_org
        m = m_org
        ans = [n_org]

        if m_org <= 1 or n_org <= 0 or n < m:
            print("Boring!")
            continue

        while n != 1:
            if n % m == 0:
                n //= m
                ans.append(n)
            else:
                print("Boring!")
                break
        if n == 1:
            print(" ".join(map(str,ans)))

if __name__ == "__main__":
    solve()