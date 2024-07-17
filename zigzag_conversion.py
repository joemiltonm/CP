def convert(s: str, numRows: int) -> str:
    if numRows == 1 or numRows >= len(s):
        return s

    # Initialize a row list to hold the characters for each row
    rows = [''] * numRows
    current_row = 0
    going_down = False

    # Iterate over each character in the string
    for char in s:
        rows[current_row] += char
        # If we are in the first or last row, we switch directions
        if current_row == 0 or current_row == numRows - 1:
            going_down = not going_down
        # Update the current row based on the direction
        current_row += 1 if going_down else -1

    # Join all rows to get the final string
    return ''.join(rows)

# Test the function with the examples provided
print(convert("PAYPALISHIRING", 3))  # Output: "PAHNAPLSIIGYIR"
print(convert("PAYPALISHIRING", 4))  # Output: "PINALSIGYAHRPI"
print(convert("A", 1))               # Output: "A"
