
# Function to calculate the maximum number of dominoes
def max_dominoes(M, N):
    # Calculate the total number of squares on the board
    total_squares = M * N
    # The maximum number of dominoes is the total number of squares divided by 2
    max_dominoes = total_squares // 2
    return max_dominoes

# Input reading
M, N = map(int, input().split())

# Calculate and print the result
print(max_dominoes(M, N))

