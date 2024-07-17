# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 
# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

nums = [2,5,5,11] 
target = 10


for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i]+nums[j] == target:
            print(i,j)


#learning enumerate
# In Python, enumerate is a class, and when you call enumerate(iterable, start=0), it returns an instance of the enumerate class, 
# which is an iterator. This iterator produces tuples containing the index and the corresponding element from the 
# iterable as you loop through it.

# converting the enumerate object to a list (list_of_tuples) allows us to see that it would produce 
# a sequence of tuples if fully unpacked. However, it's important to remember that enumerate() itself returns an iterator, not a list. 
# You can loop through this iterator using a for loop to get tuples one by one.

e = enumerate(nums)
print(e)
for i,j in e:
    print(i, j)
