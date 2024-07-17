
# https://www.youtube.com/watch?v=ngCos392W4w


# In this code, the base case returns boolean and it is propogated back to the functions first call 

# def power(n):
#     if n == 1:
#         return True 

#     if n%3 == 0:
#         return power(n/3)
#     else:
#         return False


# print(power(10))


# When designing a recursive function, you should typically consider the following key components:

# Base Case(s):

# The condition(s) under which the recursion should stop.
# What value(s) should be returned when these conditions are met.
# The base case ensures that the recursion does not continue indefinitely.
# Recursive Case:

# How to break down the problem into a smaller/simpler version of itself.
# How to call the function recursively with this scaled-down input.
# Combine Results:

# How to use the result(s) from the recursive call(s) to compute the final result for the current function call.
# This step might involve operations like addition, subtraction, concatenation, or any other operation depending on the problem at hand.



# def numbers(n):

#     if n == 0:
#         print(n)
#         return 0

#     x = numbers(n-1)
#     print(x+1)
#     return x+1

# numbers(30)

# #the below function is more straight forward



# def printNos(n):
#     if n > 0:
#         printNos(n - 1)
#         print(n)

# printNos(30)


 # finding mean of the function. 

def mean(A,N):
    if N == 1:
        return A[N-1]
    
    x = mean(A,N-1)*(N-1) + A[N-1] / N
    return x


A = [1, 2, 3, 4, 5] 

