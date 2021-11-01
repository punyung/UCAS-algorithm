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

import numpy as np


def Triangle(h, A):
    l = len(A)
    dp = list()  # 存储数组A每一小组的最小数
    ans = 0 # 三角形的顶点必须要放入

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

    for i in range(0, h):
        ans = ans + min(A[i])
    return ans


# test
h = 4
A = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
print(Triangle(h, A))
