# Input: integer array
# Output: maximum value of the sum of all subarrays
# pseudocode


def SumSubarray(A, l, r):
    # conquer

    if l == r:
        return A[0]

    # divide -> 重新递归调用函数
    # left_list = A[:n // 2]  # 左闭右开，只算0-3 ,command+?
    # right_list = A[n // 2:]
    # SumSubarray(left_list)
    # SumSubarray(right_list)
    mid = (l + r) // 2  # mid = (l+r) >> 1
    left = SumSubarray(A, l, mid)  # 左边divide
    right = SumSubarray(A, mid + 1, r)  # 右边divide

    # combine,return mamximum value
    # left
    # right
    # cross
    cross_left = A[mid]
    max_left = cross_left
    i = mid - 1
    while i >= l:
        cross_left += A[i]
        if cross_left > max_left:
            max_left = cross_left
        i = i - 1

    cross_right = A[mid + 1]
    max_right = cross_right
    j = mid + 2
    while j <= r:
        cross_right = A[j] + cross_right
        if cross_right > max_right:
            max_right = cross_right
        j = j + 1

    cross = max_right + max_left

    return max(left, right, cross)


A = [-2, 6, -1, 5, 4, -7, 2, 3]
# A = [-1, 5, -2, 7, -4, 5, 8, 6]
SumSubarray(A, 0, len(A) - 1)
print(SumSubarray(A, 0, len(A) - 1))
