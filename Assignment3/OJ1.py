# Partition Labels
# https://leetcode.com/problems/partition-labels/
# You are given a string s.
# We want to partition the string into as many parts as possible so that each letter appears in at most one part.
# Return a list of integers representing the size of these parts.
# 每个字母只出现在一个部分
# 尽可能将字符串s拆成多个部分

# def PartitionLabels(S):
#     n = len(S)
#     start = [0] * n # 记录字母第一次出现的位置
#     end = [0] * n # 记录字母最后一次出现的位置
#     pivot = S[0] # 记录用于比较的字母下标
#     for i in range(0, n):
#         for j in range(0, n):
#             if pivot == S[j]:
#                 start[i] = i
#                 end[i] = j

# enumerate 函数的用法
# 用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
# def PartitionLabels(s):
#     last = [0] * 26  # 创建一个空的list，长度为26
#     for i, ch in enumerate(s):
#         last[ord(ch) - ord("a")] = i
#     print(last)
#     # ord函数是chr() 函数（对于8位的ASCII字符串）或 unichr() 函数（对于Unicode对象）的配对函数
#     # 返回对应的 ASCII 数值
#     partition = list()  # 记录片段长度
#     start = end = 0 # 记录遍历时元素下标
#     for i, ch in enumerate(s):
#         end = max(end, last[ord(ch) - ord("a")]) #比较遍历时碰到的字母，其数组下标，取最大的
#         # e.g. 字母a的最大下标8，字母b的最大下标5，则取字母a的下标
#         if i == end: # 此时表明已经到了片段分割点
#             partition.append(end - start + 1)
#             start = end + 1
#     return partition

# 研究视频+leetcode之后，自己重新写一次
def PartitionLabels(s):
    dic = [0] * 26  # 初始化26个小写字母的字典
    for i, ch in enumerate(s):
        dic[ord(ch) - ord("a")] = i  # 存储字符串s每个字母的最后出现的下标
    # 使用贪心算法，遍历数组，找出子片段（局部最优解）
    start = end = 0  # 分别保存当前元素的起始坐标，终点坐标，用于计算最后的片段长度
    ans = list()  # 开辟一个保存结果的数组
    for j, ch in enumerate(s):
        end = max(end, dic[ord(ch) - ord("a")])  # 返回局部最长的end片段
        if j == end:
            ans.append(end - start + 1)
            start = end + 1
    return ans


# test
S = ("ababcbacadefegdehijhklij")
print(PartitionLabels(S))
