
def snake():
    n,m = list(map(int, input().split()))

    result = []

    for i in range(1, n+1):
        if i % 2 !=0:
            x = []
            for i in range(m):
                x.append("#")
            result.append(x)
        else:
            y = []
            for i in range(m):
                y.append(".")
            result.append(y)

    change_positions = []

    r1 = 1
    c1 = m-1
    
    r2 = 3
    c2 = 0

    for i in range(n):
        if r1 < n:
            change_positions.append((r1,c1))
            r1 += 4
        if r2 < n:
            change_positions.append((r2,c2))
            r2 += 4  

    for (p,q) in change_positions:
        result[p][q] = "#"

    
    for i in result:
        print("".join(i))


snake()


# Alternate solution. more precise and shows proficiency. 
# n, m = map(int, input().split())
# print("\n".join((["#"*m, "."*(m-1)+"#", "#"*m, "#"+"."*(m-1)]*n)[:n]))

    