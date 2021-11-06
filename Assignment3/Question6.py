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
    list.sort(A)
    pos = n
    ans = 0

    # m = max(A)
    # n = min(A)
    # A.remove(m)  # 删除数组A中的最大值
    # A.remove(n)  # 删除数组A中的最小值
    # ans = max(A)  # 此时提取原数组A的第二大数值作为ans
    # 如何将上述步骤变为循环？循环找最大值、最小值、第二大的数值
    # 尝试用for 循环，发现失败
    # for i in range(len(A)):  # 循环删除元素，数组大小会发生改变
    #     if i >= len(A):
    #         break
    #     m = max(A)
    #     n = min(A)
    #     A.remove(m)
    #     A.remove(n)
    #     ans = max(A)

    # 参考https://github.com/shotgun8767/ucas-algorithm/blob/master/assignment/3/6.py
    # for i in range(n//3): # 每次循环求三个最值，长度为n的数组，共需要循环n//3
    #     m = max(A)
    #     n = min(A)
    #     A.remove(m)
    #     A.remove(n)
    #     t = max(A)
    #     ans = t+ans
    #     A.remove(t)
    #     # print(ans)
    #     # print(A)
    # return ans

    # 如何做到不删除结点就能得到结果
    # Time:17min+20min
    for i in range(n // 3):
        pos = pos - 2
        ans = ans + A[pos]  # 出现调用变量为空的情况
        # print(ans)
        # print(pos)
    return ans

    # 网上查到用遍历拷贝的list，操作原始的list
    # 以下是遍历拷贝list 的demo
    # for item in A[:]:
    #     if item == 2:
    #         A.remove(item)
    #     else:
    #         print(item)
    #
    # print(A)

    # TEST


A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(maxCoins(A))
