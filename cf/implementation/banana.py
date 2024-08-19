

def banana():

    k, n, w = map(int, input().split())

    total = 0

    for i in range(1,w+1):
        total += i*k

    if (total - n) > 0:
        return total-n
    else:
        return 0

print(banana())



#use arithmetic series, mathematical approach

# def banana():
#     k, n, w = map(int, input().split())
    
#     # Calculate total cost using the formula
#     total_cost = k * w * (w + 1) // 2
    
#     # Calculate the amount to borrow
#     amount_to_borrow = total_cost - n
    
#     # If the soldier doesn't need to borrow money, return 0
#     if amount_to_borrow > 0:
#         return amount_to_borrow
#     else:
#         return 0

# print(banana())


# Total_cost=k+2k+3k+…+wk 
# Total_cost=k(1+2+3+…+w)

# sum of the first w natural numbers is:
# w(w+1)/2

