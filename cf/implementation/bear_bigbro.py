

limak, bob = list(map(int, input().split()))

count = 0

while limak <= bob:
    count += 1
    limak = limak * 3
    bob = bob * 2

print(count)

