import sys
from datetime import date

weekdays = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

def solve():
    input_data = iter(sys.stdin.read().split())

    T = int(next(input_data))
    for _ in range(T):
        M = int(next(input_data))
        D = int(next(input_data))

        pls_input_the_word = date(2011, M, D)
        print(weekdays[pls_input_the_word.weekday()])
    

if __name__ == "__main__":
    solve()
