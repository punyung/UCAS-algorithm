# 用于讨论算法，写出正确程序后，不断重复刷题理解
# Exercise1 time: Sep.27th 17:02, 用时8min38
# def FindPosition(A, l, r, target):
#     # conquer
#     if l == r:
#         if A[l] == target:
#             return [l, r]
#         if A[l] != target:
#             return [-1, -1]
# 
#     # divide
#     mid = (l + r) // 2
#     left = [-1, -1]
#     right = [-1, -1]
#     if A[mid] >= target:
#         left = FindPosition(A, l, mid, target)
#     if A[mid + 1] <= target:
#         right = FindPosition(A, mid + 1, r, target)
# 
#     # Combine
#     if left[0] == -1:
#         return right
#     if right[0] == -1:
#         return left
#     if left[0] != -1 and right[0] != -1:
#         return [left[0], right[1]]
# 
# 
# A = [3, 5, 7, 7, 8, 8, 10]
# target = 8
# l = 0
# r = len(A) - 1
# print(FindPosition(A, l, r, target))


# 2021.9.29 time:20min+8min26s
# 心得：整个算法框架思路写好了，但是在细节方面出错了，导致超出了预定目标8min26s；
# 原因是第53行和第55行的循环没有考虑到等于号的情况；Debug的过程中，找了很久才发现
# 以后，出现这种细节问题，先把断点设在递归函数的前面，判断是否有进循环里
# Input ascending array
# Output location

def ReturnLocation(A, l, r, target):
    # conquer
    if l == r:
        if A[l] == target:
            return [l, l]
        if A[l] != target:
            return [-1, -1]

    # divide
    left_list = [-1, -1]
    right_list = [-1, -1]
    mid = (l + r) // 2
    if A[mid] >= target:
        left_list = ReturnLocation(A, l, mid, target)
    if A[mid + 1] <= target:
        right_list = ReturnLocation(A, mid + 1, r, target)

    # combine
    if left_list[0] == -1:
        return right_list
    if right_list[0] == -1:
        return left_list
    if left_list[0] != -1 and right_list[0] != -1:
        return [left_list[0], right_list[1]]


A = [5, 7, 7, 8, 8, 10]
l = 0
r = len(A) - 1
target = 8
print(ReturnLocation(A, l, r, target))
