
a = int(input())
operations = []

for i in range(a):
    b = input()
    operations.append(b)

X = 0

for i in operations:
    if "++" in i:
        X += 1
    if "--" in i:
        X -= 1

print(X)


