
name = input()

unique = []

for i in name:
    if i not in unique:
        unique.append(i)

if len(unique) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")


# one liner solution
# print(["CHAT WITH HER!","IGNORE HIM!"][len({*input()})%2])
#  whenever unique items need to be collected use set data structure
