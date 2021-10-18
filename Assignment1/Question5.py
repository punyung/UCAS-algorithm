# Input: n vertices polygon
# Output: the number of ways it can divide into triangles

# def Polygon(n):
#     # conquer
#
#     if n == 2 or n == 3:
#         return 1
#
#     # if n == 1:
#     #     return print("wrong, n >= 2")
#
#     # divide and combine
#     sum = 0
#     for k in range(1, n - 1, 1):
#         sum = sum + Polygon(k + 1) * Polygon(n - k)
#         # Memo = sum
#     return sum  # 如何返回一个list
#     # 如何识别重复的那一部分
#
#
# Memo = list()
# print(Polygon(6))

# 优化过后的算法
def solve(n, cache=None):
    if cache is None:
        cache = [0, 0, 1, 1] + [0] * (n - 3)

    # Conquer
    if cache[n] > 0:
        return cache[n]

    # Divide and Combine
    ans = 0
    mid = (n >> 1) + 1
    for i in range(2, mid):
        ans += solve(i, cache) * solve(n - i + 1, cache)
    ans <<=  1
    if n % 2 == 1:
        # n is odd number
        ans += solve(mid, cache) ** 2
    cache[n] = ans
    return ans

# ----test-----
n = 6
print(solve(n, cache=None))
