import sys

def solve():

    lines = iter(sys.stdin.read().splitlines())

    T = int(next(lines))

    for _ in range(T):

        train_count = int(next(lines))

        train = list(map(int,next(lines).split()))

        times = 0

        for j in range(0,train_count):
            for i in range(0,train_count - j - 1):
                if train[i] > train[i + 1]:
                    train[i],train[i + 1] = train[i + 1],train[i]
                    times += 1
        
        print(f"Optimal train swapping takes {times} swaps.")
            
if __name__ == '__main__':
    solve()
