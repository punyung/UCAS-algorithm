# Money Robbing
# Input：value array, number of houses
# Output: the maximum value of stealing

# def Moneyrob(A):  # A represents value array
#     n = len(A)  # n represents the number of houses
#     # if n == 1:
#     #     return A
#     # 建立一个list 保存已偷取的价值,目前取值为0
#     V1 = 0
#     V2 = 0
#     # 假设第一个元素放进去
#     # for i in range(0, n):
#     #     # 如果i 放入value中
#     #     V.append(A[i])
#     #     # 卡住的点在于，如何判断接下来的价值
#     for i in range(0, n):
#         temp = max(A[i] + V1, V2)
#         V1 = V2
#         V2 = temp
#     return V2

#
# A = [1, 2, 3, 1]
# print(Moneyrob(A))


# 如果是一个圈应该如何做？

def Moneyrob(A):  # A represents value array
    n = len(A)  # n represents the number of houses
    # 建立一个dictionary 用来保存下标
    # 建立一个list 保存已偷取的价值,目前取值为0
    V1 = 0
    V2 = 0
    # 假设第一个元素放进去
    # for i in range(0, n):
    #     # 如果i 放入value中
    #     V.append(A[i])
    #     加一个数组，保存V2的下标
    for i in range(0, n-1):
        temp = max(A[i] + V1, V2)
        V1 = V2
        V2 = temp
    return V2


def Moneyrob2(A):  # A represents value array
    n = len(A)  # n represents the number of houses
    # 建立一个dictionary 用来保存下标
    # 建立一个list 保存已偷取的价值,目前取值为0
    V1 = 0
    V2 = 0
    # 假设第一个元素放进去
    # for i in range(0, n):
    #     # 如果i 放入value中
    #     V.append(A[i])
    #     加一个数组，保存V2的下标
    for i in range(1, n):
        temp = max(A[i] + V1, V2)
        V1 = V2
        V2 = temp
    return V2


A = [4, 2, 3, 7]
n = len(A)
print(max(Moneyrob(A), Moneyrob2(A)))
