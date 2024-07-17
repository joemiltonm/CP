

def candidate():
    x = list(map(int, input().split(" ")))

    n = x[0]
    k = x[1]

    s = list(map(int, input().split(" ")))

    score = s[k-1]
    # corner cases
    if s[0] == 0:
        return 0
    
    ans = []

    for i in s:
        #corner cases
        if score == 0:
            if i > 0:
                ans.append(i)
        elif i >= score:
            ans.append(i)
        else:
            exit

    return len(ans)

print(candidate())

# better solution is through using the generator expression

# def candidate():
#     n, k = map(int, input().split())
#     scores = list(map(int, input().split()))

#     # Get the score of the k-th place finisher
#     threshold_score = scores[k-1]

#     # Count the number of participants who have a score >= threshold_score and > 0
#     advancing_participants = sum(1 for score in scores if score >= threshold_score and score > 0)

#     return advancing_participants

# print(candidate())

