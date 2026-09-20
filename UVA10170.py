import sys

def solve():
    for line in sys.stdin:
        if not line.strip():
            continue
        
        S,D=map(int,line.split())
        S_,D_=S,D

        while D_>S_:
            D_-=S_
            S_+=1
        
        print(S_)

if __name__=="__main__":
    solve()