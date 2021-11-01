# Largest Divisible Subset （类似leetcode 368）

# input: a set of distinct positive integers
# output: Largest Divisible Subset
# 当我们求得所有的状态值之后，
# 可以对 f[] 数组进行遍历，取得具体的最长「整除子集」长度和对应下标，
# 然后使用 g[] 数组进行回溯，取得答案。


# class Solution(object):  # 定义solution类
#
#     def __init__(self,array):


def largestDivisibleSubset(nums):
    """
    :type nums: List[int]
    :rtype: List[int]

    """

    if len(nums) == 1: return nums
    l = len(nums)
    nums.sort()

    dp = [0 for i in nums]  # 相当于新建一个包含10个list的数组
    # dp = [[i] for i in nums]  # 新建一个跟nums 等长的list
    g = [0 for i in nums]  # 本题需要输出结果，空数组g用于记录状态转移坐标

    for i in range(l):
        length = 1
        prev = i
        for j in range(i):
            if nums[i] % nums[j] == 0:
                if dp[j] + 1 > length:
                    length = dp[j] + 1
                    prev = j
        dp[i] = length
        g[i] = prev

        # 如果 i找不到符合条件的数，则自己成为一个整除子集（如何写？）
        print(dp)
        print(g)

    # 遍历所有的dp[i] 找到最长的序列
    max_len = 0
    index = 0
    for i in range(l):
        if dp[i] > max_len:
            max_len = dp[i]
            index = i
    return max_len
    # 使用g[]数组进行回溯找答案
    result = []
    for i in range(l):
        if len(result) < max_len:
            result.append(nums[index])
            index = g[index]
    result.reverse()
    #return result


A = [9, 18, 54, 90, 108, 180, 360, 540, 720]
# ans = Solution()
print(largestDivisibleSubset(A))
