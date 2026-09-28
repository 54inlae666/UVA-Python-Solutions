import sys

def solve():
    lines =  sys.stdin.read().splitlines()
    for line in lines:
        data = list(map(int,line.split()))
        n = data[0]
        if n == 1:
            print("Jolly")
            continue
        number_list = data[1:]
        
        diff_set = set() 
        for idx in range(1,n):
            diff = abs(number_list[idx] - number_list[idx - 1])
            if 1 <= diff <= (n - 1) and diff not in diff_set:
                diff_set.add(diff)
            else:
                break

        if len(diff_set) == (n - 1):
            print("Jolly")
        else:
            print("Not jolly")
        
if __name__ == '__main__':
    solve()