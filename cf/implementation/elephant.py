# below is the worst solution

# def elephant():

#     distance = int(input())

#     step_size = [1,2,3,4,5]
#     steps = 0
    
#     while distance > 0:
#         dist = []
#         min = distance
#         index = 6
#         for i in step_size:
#             d = distance / i
#             dist.append(d)
        
#         for i in dist:
#             if i < min and i >= 1:
#                 min = i
#             index = dist.index(min)
#         distance = distance - (index + 1)
#         steps += 1

#     return steps

def simple_elephant():
    distance = int(input())
    if distance <= 5:
        return 1
    elif distance % 5 == 0:
        return distance // 5
    else:
        return (distance // 5) + 1


print(simple_elephant())


# below is the best solution. way to find ceiling
# def simple_elephant():
#     distance = int(input())
#     # Using ceiling division to get the minimum steps
#     return (distance + 4) // 5

# print(simple_elephant())




