# return the position of target
# Input: Array with ascending order
# Output: position of a target value
# example: array[5,7,7,8,8,10], target is 8, then output should be [3,4]

# pseudocode
# function FindTargetPosition(A,l,r,target)
# if l == r then
#   if target == A[l] then
#       return [l,r]
#   else if target != A[l] then
#       return [-1,-1]
#   mid = (l+r)//2
#   left = [-1,-1]
#   right = [-1,-1]
# if A[mid] >= target then
#   left = FindTargetPosition(A, l, mid, target)
# if A[mid+1] <= target then
#   right = FindTargetPosition(A, mid + 1, r, target)
# if left[0] == -1 then
#   return right
# if right[0] == -1 then
#   return left
# else
#   return [left[0],right[1]]

def FindTargetPosition(A, l, r, target):
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


A = [5, 6, 7, 7, 8, 8, 10]
l = 0
r = len(A) - 1
target = 10
print(FindTargetPosition(A, l, r, target))
