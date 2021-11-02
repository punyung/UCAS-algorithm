# Triangle
# Input：height of triangle, elements in triangle
# Output: the minimum path sum from top to bottom.
# Sample Input 1
# 4
# 2 3 4 6 5 7 4 1 8 3
# Sample Output 1
# 11
# Explanation: The triangle looks like:
#
# 2
# 34
# 657
# 4183
#
# The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (bolded above).
# 本题关键：相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。
# 也就是说，如果正位于当前行的下标 i ，那么下一步可以移动到下一行的下标 i 或 i + 1 。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/triangle
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

import numpy as np


def Triangle(h, A):
    l = len(A)
    dp = np.zeros((len(A), len(A)))

    # index = [0] * h  # 存储数组的分组索引
    # for j in range(0, h): # 尝试用这个循环拆分数组
    #     for i in range(2, 4):
    #         index[j] = j + i
    # print(index)
    # B = np.split(A, index)
    # 如何拆分数组A？？
    # 通过索引进行拆分数组？？？（研究了一个钟这玩意）
    # example
    # np.split(A,[1,3,6]) 亲测有效

    # 理解题意有误
    # for i in range(0, h):
    #     ans = ans + min(A[i])
    # return ans

    # 通过状态转移方程
    # f[i][j] = min(f[i-1][j-1],f[i-1][j])+c[i][j]
    for i in range(l):
        for j in range(0, i + 1):
            dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j]) + A[i][j]
            if j == 0:
                dp[i][j] = dp[i - 1][j] + A[i][j]
            if j == i:
                dp[i][j] = dp[i - 1][i - 1] + A[i][j]
    # 返回dp 最后一行的最小值
    ans = dp[l - 1][0]
    for j in range(l):
        if ans > dp[l - 1][j]:
            ans = dp[l - 1][j]
    return ans


# test
h = 4
A = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
print(Triangle(h, A))

# leetcode 测试
# import numpy as np
# class Solution:
#     def minimumTotal(self, triangle: List[List[int]]) -> int:
#         l = len(triangle)
#         dp = np.zeros((len(triangle), len(triangle)))
#         for i in range(l):
#             for j in range(0, i + 1):
#                 dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]
#                 if j == 0:
#                     dp[i][j] = dp[i - 1][j] + triangle[i][j]
#                 if j == i:
#                     dp[i][j] = dp[i - 1][i - 1] + triangle[i][j]
#         # 返回dp 最后一行的最小值
#         ans = dp[l-1][0]
#         for j in range(l):
#             if ans > dp[l - 1][j]:
#                 ans = dp[l - 1][j]
#         return ans

# OJ Input
height = int(input())
tr  = map(int,input()[:-1].)