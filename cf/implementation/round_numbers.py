import sys 

input = sys.stdin.read

data = list(map(int, input().split()))

result = []

for i in data[1:]:
    rounds = []
    digit_place = 1
    while(i > 0):
        digit = i % 10
        i = i // 10
        if digit != 0:
            rounds.append(digit * digit_place)
        digit_place *= 10
    result.append((len(rounds), rounds))

for (i,j) in result:
    print(i)
    print(" ".join(map(str, j)))


    






