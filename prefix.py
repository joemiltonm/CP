strs = ["flower","flow","flight"]
                
def longestCommonPrefix(strs):
    if len(strs) == 0:
        return ""
    
    if len(strs) == 1:
        return strs[0]
    
    if len(set(strs)) == 1:
        return strs[0]

    for i in strs:
        if len(i) == 0:
            return ""
    
    first = strs[0]
    
    for i in range(len(first)):
        ref_char = first[i]

        for string in strs:
            if len(string) == i or ref_char != string[i]:
                return first[:i]
    return first


# or instead of the above code, we can also use sort and then compare the first and the last string. 
# python sorted method used Timsort
# Timsort is a general-purpose sorting algorithm and can be used to sort both numbers and strings. 
# Python's built-in sorted() function and the list object's sort() method use Timsort, regardless of the data type being sorted. 
# For strings, Timsort sorts them lexicographically (akin to alphabetical order, but with all ASCII characters).
# Timsort is a combination of merge and insertion sort. 

# sorting algos are mostly either O(nlogn) or O(n^2)

# Radix Sort: A non-comparative sorting algorithm suitable for integers or strings. 
# Linear time complexity under certain conditions

# Counting Sort: Efficient for sorting integers in a specific range. Linear time complexity.
