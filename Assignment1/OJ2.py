# Input：the length of array, the number of target
#        the all elements in array and split by spaces
#        Line m+2: targets
# Output:For each target, print one line containing the starting and ending position split by spaces


def FindTargetPosition(A, l, length, target, n):  # n: the number of target
    r = length - 1

    # conquer
    if l == r:
        if target == A[l]:
            return [l, r]  # 叶结点应该返回一个列表
        elif target != A[l]:
            return [-1, -1]

    # divide
    mid = (l + r) // 2
    # left max right mini compare with target
    # prune 不需要进入递归
    left = [-1, -1]
    right = [-1, -1]
    if A[mid] >= target:  # 等于号的情况
        left = FindTargetPosition(A, l, mid, target)  # 子的作用域
    # else: # A[mid] < target, 仅包含部分情况
    #     right = FindTargetPosition(A, mid + 1, r, target)
    if A[mid + 1] <= target:
        right = FindTargetPosition(A, mid + 1, r, target)

    # combine 左边的结果和右边的结果合并
    if left[0] == -1:  # left part does not contain target value
        return right  # 有两种可能，包含target value 或 未包含
    elif right[0] == -1:
        return left
    else:  # 左右都包含target value
        return [left[0], right[1]]


A = map(lambda x: int(x), input().split())
