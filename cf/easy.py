import sys

input = sys.stdin.read

n, *a = map(int, input().split())

if sum(a) == 0 :
    print("easy")
else:
    print("hard")

    
