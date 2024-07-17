#Selection sort is a simple sorting algorithm that works by repeatedly 
# finding the minimum element from an unsorted part of the list and placing 
# it at the beginning of the sorted part of the list. 

def selection(L):

    n = len(L)

    for i in range(n):
        minpos = i
        for j in range(i+1, n):
            if L[j] < L[minpos]:
                minpos = j
            
        (L[i], L[minpos]) = (L[minpos], L[i])
    return L

#print(selection([8,7,6,5,4,3,2,1]))

# Insertion sort is a simple sorting algorithm that works by repeatedly iterating through the list, 
# comparing adjacent elements and swapping them if they are in the wrong order. 

def insertion(L):
    
    n = len(L)

    for i in range(n):
        j = i
        while (L[j] < L[j-1] and j > 0):
            L[j-1], L[j] = L [j], L[j-1]
            j -= 1
            
    return L

#print(insertion([8,7,6,5,4,3,2,1]))


def partition(L,lower, upper):

    pivot = L[lower]
    i = lower

    for j in range(lower+1, upper+1):
        if L[j] < pivot:
            i += 1
            L[i], L[j] = L[j], L[i]    
    L[i], L[lower] = L[lower], L[i]

    return i

list = [38, 27, 43, 3, 9, 82, 10]


def quick(L, lower, upper):
    if lower < upper:
        pivot_pos = partition(L, lower, upper)

        quick(L, lower, pivot_pos-1)

        quick(L,pivot_pos+1,upper)

    return L

print(quick(list, 0, len(list)-1))



  

