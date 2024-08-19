
number, subs = list(map(int, input().split()))

for i in range(subs):
    if number % 10 != 0:
        number -= 1
    else:
        number = number // 10

print(number)

