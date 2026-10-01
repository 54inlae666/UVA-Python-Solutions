

import sys

def bangle_n(N):
	if N >= 10000000:
		bangle_n(N//10000000)
		print(" kuti",end="")
		N %= 10000000
	if N >= 100000:
		bangle_n(N // 100000)
		print(" lakh",end="")
		N %= 100000
	if N >= 1000:
		bangle_n(N // 1000)
		print(" hajar",end="")
		N %= 1000
	if N >= 100:
		bangle_n(N // 100)
		print(" shata",end="")
		N %= 100
	if N > 0 :
		print(f" {N}",end="")
		
def solve():
	input_data = sys.stdin.read().splitlines()

	for n_of_case,str_fsin in enumerate(input_data,1):
		print(f"{n_of_case:>4}.",end="")
		N = int(str_fsin)
		if N == 0:
			print(" 0")
			continue
		bangle_n(N)
		print()

if __name__ == "__main__":
	solve()

