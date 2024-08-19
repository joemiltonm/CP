import sys

input = sys.stdin.read

data = input().split()


print(sum([4,0,8,20,6,12][ord(i[0])%7] for i in data[1:]))


for i in data[1:]:
    x = (ord(i[0]))
    print(x,x%7)

