# exercise 1 2021.9.26 17:50 Time: 30min39 没写出来

# def SumArray(A, l, r):
#     # conquer
#     if l == r:
#         return A[l]
#
#     # divide
#     mid = (l + r) // 2
#     left = SumArray(A, l, mid)
#     right = SumArray(A, mid + 1, r)
#
#     # combine
#     cross_left = A[mid]
#     max_left = cross_left
#     cross_right = A[mid + 1]
#     max_right = cross_right
#
#     for i in range(mid - 1, l - 1, -1):
#         cross_left = cross_left + A[i]
#         if cross_left > max_left:
#             max_left = cross_left
#         # i = i - 1
#     for j in range(mid + 2, r + 1, 1):
#         cross_right = cross_right + A[j]
#         if cross_right > max_right:
#             max_right = cross_right
#         # j = j + 1
#
#     cross = max_left + max_right
#
#     return max(left, right, cross)
#
#
# A = [-2, 6, -1, 5, 4, -7, 2, 3]
# l = 0
# r = len(A) - 1
# print(SumArray(A, l, r))

# exercise2 Time 2021.9.30 20min 无bug，答案不对;
# 原因1：for循环的下标没有搞清楚，记住range函数是前闭后开
# 原因2：cross的情况，左右没有求和

def SumArray(A, l, r):
    # conquer
    if l == r:
        return A[l]
    # divide
    mid = (l + r) // 2
    left = SumArray(A, l, mid)
    right = SumArray(A, mid + 1, r)
    # combine
    temp = A[mid]
    Sum = temp
    for i in range(mid - 1, l-1, -1): #前闭后开
        Sum = Sum + A[i]
        if Sum >= temp:
            temp = Sum
    temp2 = A[mid + 1]
    Sum2 = temp2
    for j in range(mid + 2, r+1, 1):
        Sum2 = Sum2 + A[j]
        if Sum2 >= temp2:
            temp2 = Sum2

    tempt = temp + temp2

    return max(right, left, tempt)


A = [-1, 5, -2, 7, -4, 5, 8, 6]
l = 0
r = len(A) - 1
print(SumArray(A, l, r))
