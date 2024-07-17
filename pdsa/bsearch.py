
l = [0,1,2,2,2,2,2,2,2,2,3,4,5,6,7,8,8,8, 8, 8, 9]

#below technique is throuh slicing the list. other way is recursion. 
def binary(L,F):
    low = 0
    high = len(L) - 1

    while ( low <= high):
        positions = []
        mid = (low + high) // 2
        if L[mid] < F:
            low = mid + 1
        elif L[mid] > F:
            high = mid -1
        else:
            print(low, high)
            for i in range(low, high+1):
                if L[i] == F:
                    positions.append(i)
            return mid, positions

    return False
    

m, pos = (binary(l, 2))

print(m)
print(pos)

        

