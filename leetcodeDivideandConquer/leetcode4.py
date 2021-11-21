# https://leetcode-cn.com/problems/median-of-two-sorted-arrays/
# 给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。
# 请你找出并返回这两个正序数组的 中位数 。
# 算法的时间复杂度应该为 O(log (m+n)) 。

def findMedianSortedArrays(nums1, nums2):
    m = len(nums1)
    n = len(nums2)
    if m == 1:
        return nums1[0]
    if n == 1:
        return nums2[0]
    # divide
    # 将nums1和nums2分别进行对半拆分

    # conquer
