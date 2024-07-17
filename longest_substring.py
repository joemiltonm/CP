

# # When you use enumerate on an iterable, you get back two values 
# on each iteration: the count (by default, starting from 0) and the value from the iterable.
# # enumerate is particularly useful when you need a counter 
# # with the values from the iterable, like tracking the 
# # index of items in a list while looping through it.


def length_of_longest_substring(s: str) -> int:
    char_index_map = {}
    longest = 0
    start = 0
    
    for i, char in enumerate(s):
        # this if condition is the core idea. especially comparing the index with the recent starting point. 
        if char in char_index_map and start <= char_index_map[char]:
            start = char_index_map[char] + 1
        else:
            longest = max(longest, i - start + 1)
        
        char_index_map[char] = i
    
    return longest

# Test the function with the examples provided
print(length_of_longest_substring("abcabcbb"))  # Output: 3
# print(length_of_longest_substring("bbbbb"))     # Output: 1
# print(length_of_longest_substring("pwwkew"))    # Output: 3

