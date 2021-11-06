# leetcode 1561 Maximum Number of Coins You Can Get
# There are 3n piles of coins of varying size, you and your friends will take piles of coins as follows:
# In each step, you will choose any 3 piles of coins (not necessarily consecutive).
# Of your choice, Alice will pick the pile with the maximum number of coins.
# You will pick the next pile with maximum number of coins.
# Your friend Bob will pick the last pile.
# Repeat until there are no more piles of coins.
# Given an array of integers piles where piles[i] is the number of coins in the ith pile.
# Return the maximum number of coins which you can have.

# 每次剔除数组的最大和最小值，然后再挑选数组的最大值（第一次的结果）...由此进行

def maxCoins(A):
    n = len(A)
    # m = max(A)
    # n = min(A)
    # A.remove(m)  # 删除数组A中的最大值
    # A.remove(n)  # 删除数组A中的最小值
    # ans = max(A)  # 此时提取原数组A的第二大数值作为ans
    # # 如何将上述步骤变为循环？循环找最大值、最小值、第二大的数值
    # 尝试用for 循环，发现失败
    # for i in range(len(A)):  # 循环删除元素，数组大小会发生改变
    #     if i >= len(A):
    #         break
    #     m = max(A)
    #     n = min(A)
    #     A.pop()
    # 网上查到用遍历拷贝的list，操作原始的list
    for item in A[:]:
        if item == 2:
            A.remove(item)
        else:
            print(item)

    print(A)




