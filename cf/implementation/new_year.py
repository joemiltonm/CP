

def new_year_meet():
    l = list(map(int, input().split()))

    l.sort()

    return (l[1] - l[0]) + (l[2] - l[1])

print(new_year_meet())



    

