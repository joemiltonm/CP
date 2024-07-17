def maxArea(height):
    max_area = 0  # To keep track of the maximum area found
    left = 0  # Left pointer starting at the beginning of the array
    right = len(height) - 1  # Right pointer starting at the end of the array

    while left < right:
        # Calculate the width of the container
        width = right - left
        # Find out which line is shorter
        min_height = min(height[left], height[right])
        # Calculate the area with the current pair of lines
        current_area = width * min_height
        # Update the maximum area if the current area is greater
        max_area = max(max_area, current_area)

        # Move the pointer of the shorter line towards the center
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area

# Example usage:
height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))
