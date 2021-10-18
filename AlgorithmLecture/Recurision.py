# 阶乘递归
# 递归要素：写return 条件 + 递归终止条件
# 如果递归条件没有终止，就会溢出，一般递归深度默认只有1000
def Factorial(n):
    if n == 0:
        return 1
    return Factorial(n - 1) * n


print(Factorial(5))


# 斐波那契数列递归
# 具体1，1，2，3，5,8
def Fabbonaci(n):
    if n == 1 or n == 2:
        return 1
    return Fabbonaci(n - 2) + Fabbonaci(n - 1)


print(Fabbonaci(6))
