
no_of_questions = int(input())

team_solution = []

for i in range(no_of_questions):
    sol = list(map(int, input().split()))
    team_solution.append(sol)


def sure_solution(arr):
    counter = 0
    for i in arr:
        if i.count(1) >= 2:
            counter += 1
    return counter

print(sure_solution(team_solution)) 