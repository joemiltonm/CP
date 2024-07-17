import sys

input = sys.stdin.read

n, *a = map(int, input().split())

swaps = a.index(max(a)) + a[::-1].index(min(a))

print(swaps - (swaps >= n))
