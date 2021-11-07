# Cross the River
# Some people want to cross a river by boat. Each person has a weight, and each boat can carry an equal maximum weight limit.
# Each boat carries at most 2 people at the same time, provided the sum of the weight of those people is at most boat’s weight limit.
# Return the minimum number of boats to carry every given person.
# Note that it is guaranteed each person can be carried by a boat.

# Input : the number of people; the weight limit ;  people’s weights.
# Output : The output will consist of one line containing one integer, which represents the minimum number of boats.
# Sample Input
# 4
# 3
# 3 2 2 1
# Sample Output
# 3

def CrossRiver(n, W, w):  # n代表人数，W代表船最大承重， w为list记录每个人的重量

    # wrong answer
    # 此时一直是想到两个最小值加起来
    #     ans = 0  # 记录最终需要船的数量
    #     res = [0] * n  # 记录是否上船
    #     list.sort(w)  # 对体重进行从小到大排序
    #     for i in range(len(w) - 1):
    #         if res[i] == 0:
    #             if w[i] + w[i + 1] <= W:
    #                 ans = ans + 1
    #                 res[i] = 1
    #                 res[i+1] = 1
    #         if res[i] != 0:
    #             if w[i] + w[i + 1] > W:
    #                 ans = ans + 1
    #                 res[i+1] = 1
    #         print(ans)
    #         # res[i] = 1
    #         # res[i + 1] = 1
    #     # else:
    #
    #     return ans
    ans = 0  # 记录最终需要船的数量
    j = n - 1  # 记录最大体重下标
    i = 0  # 记录最小体重下标
    list.sort(w)  # 对体重进行从小到大排序
    while i <= j:
        if w[i] + w[j] <= W:
            i = i + 1
        j = j - 1 # 为什么一定要少一个缩进？
        ans = ans + 1 # 为什么一定要少一个缩进？
    return ans


# Test
n = 4
W = 3
w = [1, 2, 3, 1]
print(CrossRiver(n, W, w))
