
no_of_statements = int(input())
operations_list = []

for i  in range(no_of_statements):
    x = input()
    operations_list.append(x)

result = 0

for i in operations_list:
    pluscounter = 0
    minuscounter = 0
    for j in i:
        if j == '+':
            pluscounter += 1
        if j == '-':
            minuscounter += 1
    if pluscounter == 2:
        result += 1
    if minuscounter == 2:
        result -= 1


print(result)

# can be solved using regex also if the input string can be in any form. helps to cut corner cases. 
#  belos could be a ideal solution

# # Read the number of statements
# n = int(input())

# # Initialize the variable x to 0
# x = 0

# # Iterate over each statement
# for _ in range(n):
#     statement = input()
#     # Check if the statement contains "++" and increment x
#     if '++' in statement:
#         x += 1
#     # Check if the statement contains "--" and decrement x
#     elif '--' in statement:
#         x -= 1

# # Print the final value of x
# print(x)


# for regex import re library and need to first compile the regex to a variable. 


