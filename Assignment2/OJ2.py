# Maximum Alternating Subsequence Sum
# The alternating sum of a 0-indexed array = the sum of the elements at even indices - the sum of the elements at odd indices
# the alternating sum of [4,2,5,3] is (4 + 5) - (2 + 3) = 4.
# Input: an array nums
# Output: the maximum alternating sum of any subsequence of nums (after reindexing the elements of the subsequence).
# 返回任意子序列的最大交替和

# 该题可利用动态规划的思想进行分解
# 子序列调整后共有两种情况，一是具有偶数个元素的子序列even[i]，二是具有奇数个元素的子序列odd[i]
# 将其设为even[i],odd[i]
# even[i] = odd[i-1]+nums[i]
# odd[i] = even[i-1]-nums[i]
# 结果为even[i-1],因为odd[i-1]一直为负数

def maxAlternatingSum(nums):
    n = len(nums)
    even = [0] * n  # 保存奇数个子序列的结果
    odd = [0] * n  # 保存偶数个子序列的结果
    for i in range(n):
        even[i] = max(odd[i - 1] + nums[i], even[i - 1])
        odd[i] = max(even[i - 1] - nums[i], odd[i - 1])
    return even[n-1]


nums = [4, 2, 5, 3]
print(maxAlternatingSum(nums))
