# Find median

def Partition(A, l, r, p):
    pivot = A[p]
    A[p] = A[r]
    A[r] = pivot
    i = l
    for j in range(l, r - 1):
        if A[j] < pivot:
            temp = A[i]
            A[i] = A[j]
            A[j] = temp
            i += 1
    A[r] = A[i]
    A[i] = pivot
    return i


def pivot(A, l, r):
    if r - l < 5:
        return Partition(A, l, r)
    for i in range(l:r):
        right = i+4
