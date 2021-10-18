# Algorithm 9 InsertionSort algorithm
# function Insertion-Sort(A,n)
# if n==1 then
# return ;
# else
#   insertionSort(A,n-1);
#   key = A[n-1];
#   i=n-1;
#   while i>=0 and A[i] > key do
#   A[i+1] = A[i];
#   i--;
#   end while
#   A[i+1] = key;
# end if

def InsertionSort(A, n):
    if n == 1:
        return
    else:
        InsertionSort(A, n - 1)
        key = A[n - 1]
        i = n - 2
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i = i - 1
            A[i + 1] = key


A = [3, 4, 1, 2,5]
n = 5
InsertionSort(A, n)
print("排序后的数组:")
for i in range(len(A)):
    print("%d" % A[i])

# Algorithm 10 MergeSort
# if l<r then

