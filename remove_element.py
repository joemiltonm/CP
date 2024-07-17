

nums = [3,2,2,3]

val = 3


def remove_ele(arr, val):    
    j = 0  
    for i in range(len(nums)):
        if nums[i] != val:
            nums[j] = nums[i]
            j += 1
    return j




        




