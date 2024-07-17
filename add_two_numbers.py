

# %: The modulo operator returns the remainder when one number is divided by another. 
# For example, 10 % 3 would give 1, because 10 divided by 3 leaves a remainder of 1.

# //: The floor division operator divides one number by another, rounds down the result, and returns a whole number. 
# For example, 10 // 3 would give 3.


x = 1001

if x<0 or (x%10 == 0 and x !=0 ):
    print(False)

reversed_num = 0

while x>reversed_num:
    reversed_num = reversed_num*10 + x%10
    x = x//10

if x == reversed_num or reversed_num//10 == x:
    print(True)



