# 678. Valid Parenthesis String
# Given a string s containing only three types of characters:
# '(', ')' and '*', return true if s is valid.
# The following rules define a valid string:
# Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# Any right parenthesis ')' must have a corresponding left parenthesis '('.
# Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# '*' could be treated as a single right parenthesis ')' or a single left
# parenthesis '(' or an empty string "".
# Example 1:
# Input: s = "()"
# Output: true

# leetcode，一个很巧妙的做法
# 遍历两次，第一次顺序，第二次逆序。
# 第一次遇到左括号加一，右括号减一，星号加一，最后保证cnt >= 0,也就是可以保证产生的左括号足够
# 第二次遇到右括号加一，左括号减一，星号加一，最后保证cnt >= 0,也就是可以保证产生的右括号足够
# 当两次遍历都是True，那么说明有效

# def checkValidString(s):
#     def help(a):
#         cnt = 0
#         for c in s if a == 1 else reversed(s):  # a取1时，顺序遍历；a取2时，逆序遍历
#             if c == '(': cnt += a
#             if c == ')': cnt += -a
#             if c == '*': cnt += 1
#             if cnt < 0:
#                 return False
#         return True
#
#     return help(1) and help(-1)


# 作者：NobiShinnosuke
# 链接：https: // leetcode - cn.com / problems / valid - parenthesis - string / solution / tan - xin - zhi - jie - zhuan - hua - xing - hao - by - no - 96j
# 6 /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# reference: https://leetcode.com/problems/valid-parenthesis-string/discuss/543521/Java-Count-Open-Parenthesis-O(n)-time-O(1)-space-Picture-Explain
# 这个方法比较难理解，大意是：由于我不知道 * 可能是哪种情况，所以我干脆在遍历的过程中讨论所有可能的情形，具体操作如下：
# （必须结合连接中的图进行理解）（虽然这个方法很难想，但 Leetcode 上 Discuss 的前三都是这种方法及其变种，所以还是得掌握）
# 1. 用 cmax 保存直至当前字符，在所有可能分支中，待匹配的 '(' 的个数的最大值
# 2. 用 cmin 保存直至当前字符，在所有可能分支中，待匹配的 '(' 的个数的最小值
# 遍历字符串：
# 1. 若当前字符为 '(' ，则 cmin 和 cmax 都自增 1
# 2. 若当前字符为 ')' ，则 cmin 和 cmax 都自减 1。若 cmin < 0，则令 cmin = 0，即抛弃那些不成立的分支
# 3. 若当前字符为 '*' ，对应了三种可能的情形：
#    a. '*' 取 '(': cmax 自增 1
#    b. '*' 取 ')': cmin 自减 1
#    c. '*' 取 '': 无变化
#    由于要同时考虑以上三种情况，所以在此分支下，cmax 自增 1，cmin 自减 1
# 4. 在进行上述操作后，如果 cmax 小于 0，则意味着没有任何一个分支满足题目的要求，直接返回 False
# 遍历字符串后，cmin 为 0 则表明有至少一条分支满足：无待匹配的 '('，故返回 True
# 如果 cmin > 0，表明没有一条分支满足无待匹配的 '('，故返回 False
# def checkValidString(s: str) -> bool:
#     cmin, cmax = 0, 0
#     for c in s:
#         if c == '(':
#             cmin += 1
#             cmax += 1
#         elif c == ')':
#             cmin -= 1
#             cmax -= 1
#         elif c == '*':
#             cmin -= 1
#             cmax += 1
#         if cmax < 0:
#             return False
#         if cmin < 0:
#             cmin = 0
#           return True


def checkValidString(s):
    cmin = 0
    cmax = 0
    for c in s:
        if c == '(':
            cmin += 1
            cmax += 1
        elif c == ')':
            cmin -= 1
            cmax -= 1
        elif c == '*':
            cmin -= 1
            cmax += 1
        print(cmin)
        print(cmax)
        if cmin == 0:
            return True
        if cmin > 0:
            return False
        if cmax < 0:
            return False


# test
s = "(*)"
print(checkValidString(s))
